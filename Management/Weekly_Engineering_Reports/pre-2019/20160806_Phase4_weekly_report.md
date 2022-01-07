DEFCON 24

Our Talk at Wireless Village! Awesome photo of us presenting credit due to John GI7UGV @radwire on twitter.

Our talk at DEFCON Wireless Village was very well attended and very well received. Skunkworks, Abraxas3d, and TBD all represented Phase 4 on Saturday afternoon. We got the first speaking slot after the shock collar equipped SDR dogfight contest. If the speaker names for this talk sound unfamiliar, it's because they are our not-so-secret hacker handles. Skunkworks is Paul KB5MU. I'm Abraxas3d, and TBD is Steve Conklin. That handle literally is TBD because he hasn't told me his secret hacker handle yet. It's obviously highly classified. We talked fast about phase 4 in our 20 minute time slot. The slides are in our github repository. 

We emphasized the experimental possibilities and the fact that we are solving lots of small problems and kicking them out to the community along the way. TBD announced the user synchronous web app, which was a big highlight for me. If you haven't checked out the software yet, then please do. TBD aka Steve Conklin described it in an email to the Phase 4 Ground list. It's great. Other topics were authentication and authorization, generic stream encapsulation, and why a dual-band feed is both challenging and useful. 

DEFCON Wireless Village is where SDR enthusiasts and signal freaks hang out. It has its own speaker track, its own competitions, and its own social events. In any other town, it would be a convention in its own right. It's also the go-to place for gearing up for the very successful DEFCON ham radio exam session. Seeing hardcore hackers that almost all have a problem with authority get probably the most old school toe-the-line type of license from the government - the FCC no less! - is thoroughly entertaining. The ham radio exam sessions at DEFCON24, and yes it's been going on for 24 years, were sponsored by hackers from area code 408. 

Shorthand for these sorts of groups is the letters DC followed by the area code. For example, DC408. Identifying with your area code and forming a group based on your area code dates back from when the phone system was a primary target of many hackers or phreakers, spelled with a ph from the word phone. DEFCON supports the organization of groups based on area code, and many of these groups then sponsor or run events at DEFCON. If you want to find out if you have a defcon group near you, then check out the link in the notes. 

https://defcongroups.org/

The ham radio exam results for this year: 95 Technicians 22 Generals and 11 Amateur Extras. 

The Badge Life

DEFCON has had electronic hackable badges for many years and this year was no exception. In some years, the badge is part of a hacking challenge or competition. I've done this at least twice. For DEFCON 17, we grafted on a Muller tube, read the resulting radioactive measurements as a random number generator, and used that to create a secure link to another badge. The writeup can be found at the link in the notes. 

http://www.bigideatrouble.com/dc17badgehack.pdf

For DEFCON 18, we did a project that is not safe for work to describe with the badge. It involved audio and video and was a lot of fun. The processor that year was a digital signal controller. There weren't a lot of input and output available on the board, so we had to get cracking on how to do ambitious things with limited IO. 

Some years, such as DEFCON 23 and 19, and most before 15, the badge is not electronic. For 23 it was literally a 45 record. Yeah. You had to wear a white 45 record around your neck for like 5 days. I drew a clock on mine and cosplayed Flav o Flav. And, guess who actually showed up at the hotel for photos? Yeah. Flav o Flav himself. 

These sorts of project is representative of badge hacking efforts at DEFCON. If you choose to do this sort of activity or contest or challenge, then you are almost completely dedicated to this project for the duration of the convention. The payoff can be very big, as the winning team gets a coveted Black Badge, which gives DEFCON admission for life. Aside from the prize, the opportunity to hack with your friends in a Las Vegas hotel room turned into a lab is totally fun, and the mystery of what hardware will be on the badge isn't revealed until the convention, so you have to be flexible, bring your best guess of tools, or be able to come up with the right tools and equipment in short order. You have only a few days, and with so much else to do, the time flies by. 

In other years, like 2016, the badge is indeed electronic, but the badge competition is a puzzle with clues either written on the badge or lanyard, or transmitted over serial port when buttons are pressed, or in the firmware itself. One year, a big clue was tucked away into "unused" memory. The competition does not involve any hardware hacking on the badge itself. This past year, the skull badge had a D2000 Intel processor, eight buttons, and a serial port. Pretty simple, but your job as part of the DEFCON nation is to take that badge and do something cool with it. The possibilities are myriad. One could make a game controller or a drone controller or a forklift hijacker or whatever. 

So what does this have to do with amateur radio? 

Well, Steve and me and Paul and a few others in the weeks since DEFCON have given some serious thought to making a Phase 4 Badge project. This badge would be amateur radio capable, could serve as really fun thing to take to amateur radio conventions, could be sold as a fundraiser, allows you to contact others - yes actual QSOs - and interact with others, is hackable or modifiable, and could - this is the best part - seriously provide additional functionality to radios that you might be interested in owning. We're in the early stages but if you are interested in a Phase 4 Ground sponsored amateur radio badge, then let me know and we will exploit your skills. And money. We are going to need a couple thousand dollars for this to get it designed the right way. 

Competitions Completed!

Congratulations to Skunkworks, aka Paul KB5MU, who completed the Hardware Hacking Village reverse engineering challenge. This consisted of showing up, standing in a long line, paying $2 for a bag of parts, soldering the parts together, and figuring out at least four challenges. Once the circuit was up and running, an LED on the board blinked four times.  With every challenge unlocked, the LED on the board would blink one less time. So when you solved the first challenge, it would blink three times. Then two. Then one. Then it would stay lit. Paul won an Arduino Uno as a prize along with DEFCON street cred and had a lot of fun along the way. The circuit was a small PIC micro controller with a tiny board with lots of extra traces to confuse reversing how all the pins were connected. The first challenge involved cutting a trace that just so happened to be (you guessed it) under the chip. How are your desoldering skills these days? Solder wick can be your friend. Other parts of the challenge involved ciphers, I2C, and downloading the ROM, changing part of the disassembled code, and reprogramming the chip. There was a PicKit3 station at the hardware hacking village. If you're in the market for a PicKit3, then you have a moral obligation to watch these two YouTube videos. Links in the notes. Watch them in order. Otherwise it won't make sense. 

https://www.youtube.com/watch?v=LjfIS65mwn8

https://www.youtube.com/watch?v=3YUvlrVlNao
