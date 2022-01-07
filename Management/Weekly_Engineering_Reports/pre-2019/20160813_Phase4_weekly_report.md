Generic Stream Encapsulation is a DVB protocol that handles incoming digital data and produces DVB frames ready for transmission over the air. It was introduced with the second generation of DVB standards and is much more efficient and flexible than using MPEG.

David kb8kzm has stepped up to help with the Python implementation of GSE, and this is really good news. Thank you David! If you know Python, want to learn Python, are an expert in Python, or anything in between, and can help us complete this part of the project, we can really use the help. 

Why do this? Coding GSE in Python gives us an implementation that allows us to test our theories on making GSE better fit amateur radio. It gives us something to compare production code against. This should improve our verification and validation stages. It also enables testing of other components of the system. 

We are going to need GSE "real soon now" because we are about to test actual real modulators for the DVB downlink. We really want to be able to feed in data that is encapsulated with GSE. Why write our own? We need to make some modifications that make it work for amateur radio, rather than satellite broadcast. You want to be able to monitor, filter, and respond to stations. You're not just a passive receiver, you're not the only recipient of the data, you're going to want some fundamental freedoms within the system, and making sure that the structure of the data frames properly supports amateur radio functionality without breaking DVB compatibility is a requirement. 

So here's the repository for Phase 4 GSE. 
https://github.com/phase4ground/GSE
What we did here was move the documents and Python programs to their own repository, out from under the software folder in Phase 4 Ground Documents. 

We're starting with the encapsulation. Packetized data of any type comes in, and DVB frames go out. DVB-S2/X is what we're starting off with, but for terrestrial transmission from the Groundsat, the frames would be DVB-T2. What goes up, must come down. So keep in mind, de-encapsulation has to be done too! 

We expect IP packets are what we're going to be dealing with as input, but that actually isn't a requirement. GSE allows us to handle pretty much any sort of data that's being thrown at us.

The first attempt to get work done here started with the incoming data. After talking it over in an early design review with Paul KB5MU, the suggestion was made to start with the desired output, write that code, and then write backwards towards the input. 

There's a block diagram from the GSE standards documents from the DVB project that can be used to establish classes and objects. Things started making more sense. My recommendation here is to go ahead and use this block diagram, set up Python objects that are partitioned pretty much like this, and get to work on defining the behavior. The objects all work together just like the blocks in the block diagram. 

It sounds more simple than it is, of course, since anything in coding is way harder than it appears in the sideview mirror.

Michael Ossman recommended using the bitstring module https://scott-griffiths.github.io/bitstring/ 

This was a big help. This module was a huge improvement over trying to use structs for frames. Bitstring allows fields with odd numbers of bits and has built-in functions that make handling the construction and interpretation of the frames way more easy than it would have been if we'd stayed with stucts. 