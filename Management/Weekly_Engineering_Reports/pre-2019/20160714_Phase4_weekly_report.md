
Dual-band feed prototyping continues by Paul Wade W1GHZ. Me and others are ready to 3D print and or machine some more as soon as the model is released. We very much appreciate Paul's time and effort and expertise on this! 

Steve Hicks and I talked about next steps in the adventure of building development and production hardware at Flex Radio. He's going to find out how much it would cost to get some small number of development boards, and my job is to figure out how big of an FPGA we really need. 

Another contender for building all or some hardware for phase 4 is on the team. 

I'm asking Bob N4HY to help with this question in kind of a roundabout way. We both have Red Pitaya boards, with the Zync 7010, and we want to know how many demodulators and how big of a polyphase filter bank can be stuffed into this smaller FPGA. 

Learn more about these really neat boards here:
http://wiki.redpitaya.com/index.php?title=Main_Page

Quick start page is here:
http://redpitaya.com/quick-start/

If we can get a better handle on the size required for a DVB-S2X/DVB-T2 design then we can start seriously selecting and pricing FPGAs. FPGAs are expensive and the pricing is weird. 

Another angle explored this week during an informational interview is the possibility of building or using DSPs somewhat opposed to FPGAs with dedicated coprocessors to do the heavy lifting. 

Here's a very useful link: http://www.ece.rice.edu/~ys4937/distribute/2010-Book-Springer.pdf

Calculated phase noise numbers from Kerry Banke N6IZW are in the repository. These are what is expected to be the phase noise for an LO based on the ADF4350. The ADF4350 is a wideband synthesizer with an integrated VCO. Check out the data sheet here:

http://www.analog.com/en/products/rf-microwave/pll-synth/adf4350.html

Kerry will take measurements as soon as possible and these measurements will be added to the document in the Performance folder in the github repository. As always, the repo is here:

https://github.com/phase4ground

We remain in a place where we need volunteers to write GNU radio DVB-S2, S2X, and T2 receiver blocks. We cannot provide the sort of recipes that we want to provide to the community without a GNU radio flow graph. Figuring out whether and how to modify the existing demodulation and decoding blocks in GNU radio is good first step. 

On the GNU radio transmitter side, there's some good news. DVB-S2X transmitter updates have been checked into the GNU radio project by Ron Economos aka Dr. MPEG. He is the author of the content in the DTV GNU radio module. He explains that the Physical Layer Framer block will need to be significantly updated to complete the VL-SNR transmitter. 

On the HDL side, here's an open source receiver board project that needs some review to see if we can use it to bootstrap our receiver. 

http://www.netup.tv/fr-FR/documentation/articles/universal-open-source-dvb-card
https://github.com/aospan/NetUP_Dual_Universal_CI-fpga

Our efforts to implement Generic Stream Encapsulation will pay off here because GSE would need to be grafted in to this codebase. Anyway, check it out and weigh in on the list. 

If you are a member of AMSAT, then you have received your AMSAT Journal, and you might have noticed a lot about Phase 4 and Dayton in that issue!

Dr. MPEG writes "After seeing the K3IO, N4HY and KM4KAL article in the latest AMSAT Journal, I've created a DVB-S2 with SSB flow graph that's a lot more functional. You can download it from my website. http://www.w6rz.net/dvbs2_ssb.grc"

The test video stream for 3.072 Msym/s 5/6 8psk is here. http://www.w6rz.net/drinky8psk.ts 

Oh yeah, you have to build and install his Controlled Envelope SSB (CESSB) out-of-tree module.

https://github.com/drmpeg/gr-cessb 

He says "With the center frequency at 52 MHz, the SSB ends up on 50.125 MHz. You can just start to hear the 8psk waveform at around 50.160 MHz. I'm using an Icom IC-7300 as the receiver with a 30 dB attenuator. Both the SSB and DVB-S2 signal are around S-9."

Speaking of AMSAT, please join! 

If you want to contribute to Phase 4 Ground then join the mailing list by applying at 
http://www.amsat.org/?page_id=1121.I found out how to get a terrain profile in google earth. Here is a set of them between some of the places we want to use for prototyping equipment. The Palomar mountain end of the control link, using Ubiquity hardware, is up and running. This is a great utility that happens to be free in google earth.

DEFCON Wireless Village asked for more information about the project in order to evaluate us for a speaking spot. The deadline is Friday, so I'm working on that and will report back as soon as I hear anything. 

More soon! Gotta catch 'em all!