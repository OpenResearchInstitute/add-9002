Greetings all!

Plenty of progress on the 5GHz uplink RF Chain. If you haven't seen the engineering report from last week, then check it out in the link below.

https://youtu.be/5XKWHTc8xCI

Some additional information about the uplink is that measurements of the second order harmonic for the Skyworks solution turned out to be -42.5dBc. There is a lot of optimism about this solution, and I'm hoping we can show off the progress at Dayton.

Speaking of Dayton, team planning for our presentation on Friday evening at the TAPR/AMSAT dinner, and at the booth in the hall, will kick off on Monday. There are several people that have volunteered to help present at the dinner, and we will work out who says what over the next week or so. This will be a fun and accessible talk!

If you're at Dayton and infiltrating another event, know that our home base is most likely going to be the AMSAT booth in the hall. Please feel free to come by and leave a message or hang out. I'll be there with as much stuff as I can bring and will make a point of occupying the booth. You know, to defend it from the Red Team.

There is a conference coming up at Virginia Tech. It's a Wireless Symposium. Here's the link. I'm thinking about going, which means I still have to ask my housemates, but might have already registered. Don't rat me out. If you're near VT or at VT, then let's meet up and hammer out some Phase 4 Ground details. Here's the link to that conference.

https://wireless.vt.edu/symposium2016.html

The google forms method for cutting up work continues with two new initiatives this week. We kicked off a Dynamic QSL card project, and got a team leader and team formation. This effort is the first web app for Phase 4 Ground, and produces a beautiful visualization of logged contacts between one or more stations. This is an algorithmic graphical arts project that will blaze a trail into our web app methodology. Phase 4 ground will not have traditional software packages. You will use web apps, either in the cloud, or served directly from the radio. to access the radio. You will be able to write your own, if we get our act together and document it well enough. Which, is the intent. A big thank you to Steve Conklin for stepping up and taking on this job. Figuring out web app radio stuff is nontrivial and will provide a large amount of leverage for all the other apps that we envision, ranging from your regular rag chew app to emergency communications ICS forms apps to apps that monitor or filter or alert you to communications opportunities or situations. This is important stuff.

Another task that kicked off this week is the receiver GNU radio blocks definition project. I have one volunteer here besides myself, and am looking for more.

http://goo.gl/forms/fjYftDxWNB

This is the effort that will specify what the blocks for our open source receiver do. The implementation is another task, possibly done by the same people, but not necessarily. Our job is to take the DVB-S2/X standard and specify what blocks are needed in GNU radio in order to provide the functionality required. We're doing an adaptive coding and modulation version of DVB-S2/X. Our stream management is the DVB Generic Stream Encapsulation protocol, which is simpler and lighter weight than using MPEG streams, and directly frames up IP traffic for shipping over Phase 4 Ground.

Importantly, the modulations that we're using already exist in GNU radio. This process will identify blocks that already exist as well as specify blocks that are needed. We will not be reinventing any wheels. If we need new rims, though, we'll make that happen.

We will be implementing as much as possible as RFNoC, which stands for radio frequency networks on a chip. We've gotten a lot of support and encouragement here, and it's just too amazing of an opportunity to pass up.

RFNoC is to FPGAs as GNU Radio is to general purpose processors. For most flow graphs and SDR implementations, there is limited ability to modify the code for the FPGA. RFNoC provides a framework and workflow to partition radio designs between the processor and the FPGA in a way that actually utilizes the FPGA. The problem that we're having in SDRs right now is exactly that - an underutilization of the FPGAs.

https://github.com/EttusResearch/uhd/wiki/RFNoC:-Getting-Started

There are expensive and there are not as expensive ways to get into FPGA design. We're actively discussing and reporting development and evaluation boards that allow entry level into FPGA radio development. Two that we discussed this week are the Kickstarter success Spartixed and the commercially available Red Pitaya. The Red Pitaya has ADC/DAC I/O - two channels in fact - and sports a small Zync system on a chip. The Zync, as you probably know, is a combination of an ARM processor and programmable logic fabric. Being on the same chip, you get a substantial performance bonus.

http://referencedesigner.com/tutorials/s6evalboard/eval_board_02.php

http://wiki.redpitaya.com/index.php?title=Hardware_Overview

This is a very exciting time for amateur radio digital microwave and satellite. If this is something that interests you or you feel like you want to support it, then join ARRL, AMSAT, and TAPR. Projects like Phase 4 Ground simply can't exist without the support and promotion of these organizations. If you want to join our team, please contact me or go to the link in the notes to apply. All our work is open source on github. Search for Phase Number 4 Ground. Link in the notes!

https://github.com/phase4ground

Author alert: Our very own Eric Nichols KL7AJ has written a book "Digital Storage Oscilloscopes for Ham Radio", which is available here:

http://www.arrl.org/shop/Digital-Storage-Oscilloscopes-for-Ham-Radio/

More soon!