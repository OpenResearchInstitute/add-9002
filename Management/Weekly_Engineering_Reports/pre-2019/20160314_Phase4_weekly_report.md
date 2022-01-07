Happy Belated Pi Day!

Air Interface Progress

There has been some. We have progress. We have questions. Here’s the rough drafts. A deceptively simple question is whether or not to force everything to be IP. IP is what GSE assumes. We do, however, have the option of allowing non-IP traffic through in an intelligent manner. What sort of traffic might this be? It could be traffic flagged as legacy traffic from an ARAP. It could be our own custom baseband recipe. It could be almost anything, but it has to be something worth transporting, worth differentiating, and worth processing. We're looking for feedback here for sure. 


Satellite Class

I took a class on the design of satellite links that involved using geosynchronous satellites to provide internet access to customers on airplanes. It was through the IEEE communications society, was taught by a very qualified person, and was three hours long. I learned that our choice of DVB-S2 is totally right on target. I learned that antennas are really hard to design for things that move fast and might get hit by birds. I learned that the sorts of things we're worrying about are absolutely the sort of thing we should be worried about, and that's pretty much it. I learned about who the major players are in the GEO strata, and I learned that the entire provide-internet-access-to-planes market has yet to fully take off. Pun intended. I'm showing the notes I took during the class, but honestly, this class simply reinforced the directions we're taking and the decisions we're making. We have our work cut out for us, but we are on the right track. 


authentication/authorization progress

Substantial progress has been made on defining what the default authentication and authorization schemes for Phase 4 Ground radios should be. Our goal is to have a scheme that works out of the box, that has clear and easy-to-use instructions, and that supports more complex or restrictive authorization without friction. This is not an easy problem. Fortunately, we have some very competent people on our side. The discussion this week began with a summary of informational interviews and a core concept that leverages the authentication provided by Logbook of the World. 


Outernet setup experiences by Paul KB5MU. Here's some video, and he's written up a report of his experiences and their relevance to Phase 4 Ground.

Snow on Palomar on top of our experiment (how rude) Here’s what snow on microwave equipment looks like. We’re ready to receive the signals from the matched set of gear at Dixon. 


Modulation Mismatch

The bid to commit to "real" DVB-S2 instead of a modified version that changes QPSK to OQPSK has been resolved. Space segment will use QPSK, which aligns with the DVB-S2 standard, instead of OQPSK. The impact to the PA is considered to be insignificant at this time. Thank you space team! The next step is to get positive confirmation that 90 degree BPSK can be used for the PLHEADERS, which stands for Physical Layer Headers in DVB-S2. This last confirmation is the only remaining obstacle to a fully compliant DVB-S2 modulation scheme. We expect to use 90-degree BPSK, QPSK, and possibly 8QPSK for Phase 4B. 


Dayton hamvention planning has begun. 

The RSVP form is available at the link in the notes.
http://goo.gl/forms/Yyy1YMdHLU

The slides for the talk at the Dayton TAPR/AMSAT dinner have been started! If you are there, you are welcome to speak with me! Click on the link in the notes and sign up. If you want to infiltrate the Flex dinner instead, or establish a beachhead somewhere else, then let us know! Click on the link and sign up. Or make some catty comments. 

I’m planning some fun trinkets and enjoyable keepsakes for distribution at Dayton. Phase 4 Ground has space at the AMSAT booth at Dayton, and we will use the AMSAT booth for coordinating meetups and posting pithy remarks, things like that. 


HackRF updates are many and will be in the next report. 


Howie DeFelice is the lead for one of the payloads we are tasked to support. It’s called CQC, which stands for Cube Quest Challenge. This is a completely awesome project that sends a spacecraft to the moon to compete against other projects in how much data can be sent back. If you want to join this project, then you are in for a big treat. This is space cowboy/girl stuff at its best. The link in our end bumper will take you directly to the AMSAT engineering volunteer page.  

Anyway, Howie went to the super awesome DC area satellite show, and he wrote a great report. There are several companies showing off DVB-S2X gear that we might be able to use. His report will allow those of us on the Ascent team to begin to follow up and evaluate whether any of these commercial systems would be appropriate for us! Sounds like a fantastic show. I wish I could have been there. 


Pointing Assist Project

Bill Werner reports progress on pointing assist. He is able to get 1 degree resolution on a hardware pointing assistant. With the beam width of a 10GHz DSS style dish on the order of 2 degrees, this is a great start. I’m hoping to coordinate some VT students in making pointing assist circuits out of the boards that I got from SparkFun. Paul KB5MU believes that if we can possibly use a commercial SatFinder (available from amazon at low cost) that this might be another way to help people orient their dishes successfully. What the SatFinder might have to do is find a commercial satellite near enough to us that it would provide meaningful pointing assistance.

It should be obvious from the Outernet experiences that pointing a dish sometimes requires real customer service. At a minimum we must provide clear and relevant documentation, and we need to start thinking about how we provide technical support, in the case where pointing is impossible due to an equipment failure or shortcoming. 

This brings up something long-term and critical to our success, which is technical support and customer service in general for Phase 4 Ground.

It is not in the mission of Phase 4 Ground engineering team to provide long-term technical support or customer service. Where do these functions belong? Where does technical support and customer service come from? 

Many of us will indeed participate fully in the community of users, but I think we all have experienced varying levels of satisfaction of the help we’ve gotten from community forums. If you’re like me, then you believe that these sorts of questions need to be considered from the beginning, and not suddenly an issue after sales begin. 

My job is to figure out what the right path forward is for us. This isn’t settled at all, so I’m very interested in getting the the widest possible feedback I can in order to best advise AMSAT of what they’re incurring with a manufactured solution and a set of recipes. 

If we develop and maintain very good documentation, then that’s one of the necessary conditions for customer service and technical support success. By itself, though, it might not be sufficient. 

John Klingelhoeffer sagt meine Aussprache seines Namens war falsch. Entschuldigung John! Ich dachte, es war Kling el ho ef er. Er sagt Kling el Hay fer aber es ist ein Umlaut, nicht wahr? Oe nicht Ae? Ich werde probieren, es richtig zu machen. (We actually call him Klingelhooper at my house, but don't tell anyone).

Your opinions are sought on this and all the other subjects raised this week. Thank you for being part of the project! If you haven’t joined AMSAT and ARRL then you should. Your membership makes this project, and many many others, possible. Let them know why you’ve joined and you’ve raised our visibility as well. 


