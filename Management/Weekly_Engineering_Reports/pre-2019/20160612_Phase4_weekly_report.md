As you can see (from the video), Wireless@VT was a lot of fun and a huge success. It wasn't all fun and games, we did actually get some work done. The farthest-reaching initiative was an agreement to write an MOU between AHA, Virginia Tech, Ettus Research, and AMSAT in order to work on RFNoC blocks oxf AHA's DVB-S2X implementation. There has been progress on this over the past week. There will be a meeting June 22nd to review the MOU and set a date for the RFNoC HackFest. This will help the payload team tremendously. 

The goal is to have the forward error correction done by GNU Radio Conference in September. The payload team wants to present at GNU radio con and Phase 4 Ground has applied for time at DEFCON. 

Since last week, we started looking at LDPC blocks in GNU radio and writing down notes. Ron Economos W6RZ is the author of the DVT module in GNU radio. I asked him some questions about his LDPC block, and he not only answered them fully, but also said he'd be happy to complete the DVB-S2X functionality in the LDPC encoder in the DVT module. 

Thank you Ron! 

We'll need a decoder. We'll need to try to get it into RFNoC, and in addition to that , we'll need a whole pile of other things, but progress here should be celebrated. Please go read how to make an out of tree module in GNU radio. We need people that can code in python and C++ and we need people that can code in verilog or vhdl to convert blocks into HDL. 

Link to the tutorial is in the notes.

http://gnuradio.org/redmine/projects/gnuradio/wiki/OutOfTreeModules 

Another big step forward in Virginia was the successful preliminary design review for the Phase 4B payload team. This was a few days before the conference, but I had an opportunity to attend the regular Friday meeting in person and talk about how the review went and about the next steps. Sanitized version of the slides is said to be forthcoming. There was a followup meeting on Tuesday but I'm on jury duty and missed it. 

Shifting gears to another continent, we have reached out to AMSAT-DL about the Phase 4A payload, and whether or not we can support their downlink with our Phase 4 Ground project. The contact was positive and more discussion will occur. Here's a technical brief about Es'hail Phase 4A project. This payload will not be visible from North America. If successful, a payload further east, visible from Japan, will possibly be launched. 

Supporting these payloads increases our market and opportunity for technical collaboration with amateurs around the world. 

-=-=-=-=-=-=-=-=-=-=-=-=-

https://amsat-uk.org/2016/05/21/eshail-2-geo-p4a-transponder-freqs/

Wideband digital transponder
 2401.500 -  2409.500 MHz Uplink
10491.000 - 10499.000 MHz Downlink

Equipment requirements:

X-Band 10 GHz Downlink:
– 89 cm dishes in rainy areas at EOC like Brazil or Thailand
– 60 cm around coverage peak
– 75 cm dishes at peak -2dB
– NB: linear vertical polarisation
– WB: linear horizontal polarisation

S-Band 2.4 GHz NB-Uplink:
– narrow band modes like SSB, CW
– 5W nominal Uplink power (22.5 dBi antenna gain, 75cm dish)
– RHCP polarisation

S-Band 2.4 GHz WB-Uplink (DATV):
– wide band modes, DVB-S2
– peak EIRP of 53 dBW (2.4m dish and 100W) required
– RHCP polarisation

Presentation on Es’hail by Peter Guelzow DB2OS, President of AMSAT-DL, at the 2013 AMSAT-UK Colloquium 

http://www.batc.tv/streams/amsat1306

AMSAT-DL Es'hail Phase 4A update Peter Guelzow DB2OS and Achim Vollhardt DH2VA give an update of AMSAT-DLs projects at the AMSAT-UK International Space Colloquium in Guildford on July 25, 2015. 

https://www.youtube.com/watch?v=vxBtTymzKSA July 2015

-=-=-=-=-=-=-=-=-=-=-=-=-

As you can see from the technical brief above (in the notes), the uplink frequency is 2.4GHz, not 5GHz. 4A uses a commercial DVB-S downlink. 4B uses DVB-S2X. S2X is backwards compatible with DVB-S, but anyone who's ever worked with backwards compatible systems knows that this doesn't just happen. It takes work and care. 

4B uses generic stream encapsulation. 4A uses 1 mpeg transport stream. 4B downlink is up to 10MHz. 4A seems to be set to 8MHz. 

If you follow the links in the 4A notes above, then you can review a list of suggested hardware. These suggestions may also work for us. 

Modifications for a cheap LNB (in french):
http://f1chf.free.fr/LNBPLL/

sr-systems with DVB-S demodulators and decoders. This is nice commercial gear. It seems to be designed to get the mpeg transport stream and then decode it to audio and video. What we're after is something a bit different. We use the generic stream encapsulation in order to transport data. The MPEG transport stream is just that - a transport stream for television signals. GSE encapsulates IP traffic. Our traffic is mixed modes. Voice, voice memo, documents, text, data, video, whatever that can be transported. IPv4, IPv6, whatever. So I wrote sr-systems.de asked if these products support GSE. The response seems to be yes. "If you have the GSE Encapsulation, you can set our Modulator to "BB Frame only" and connect your GSE Stream over our ASI-IN On the MiniMOD4." I will follow up to make sure I understand what is required. This may be a viable recipe. 

Phase 4A people are also working on a dual band feed. This is 2.4GHz/10GHz. Their primary concern is the 10 Watt uplink amplifiers sitting right next to the downlink LNA. They do not have the same second harmonic problem that we do, but this sort of dual band feed is still challenging and they are calling for volunteers to help out here. 

Other gear discussed includes:

3cm downconverter from Kuhne. The MKULNC 10 CON with an intermediate frequency of 70cm. 20dB gain, 1.2dB noise figure, female SMA input and N connector output 320 euros. This seems to have only 2MHz of bandwidth, so my feeling is that this is being recommended for the linear transponder.

Then, there is an X band low noise amplifier from Kuhne. MKU LNAs 102 S EME super low noise pre-amp? 10318 - 10418 MHz frequency range? 22dB of gain with a 0.7 noise figure? Waveguide in and female SMA output? Milled aluminum case? 240 euros? Yes please. 

There's a nice 60 cm dish from PROCOM with 31dB of gain, 4 degree beam width. It's the PRO-10-001/50. 

Phase 4A spacecraft EIRP is assumed 30dBW with 50 channels. This means 12.5dBW per channel. There is 205 dB path loss. The ground G/T is 14 dB/K and a C/No of 50BHz. Channel bandwidth is 2.5kHz and that means 15.4 dB carrier to noise per user. These numbers are from the presentation linked above and are in line with assumptions for phase 4B. Phase 4A will use a linear horizontal downlink polarization. This is in line with our linear polarization decision. 

The emphasis for Phase 4A on education is very much in line with the emphasis on education for phase 4B. That the justifications align should surprise no one. 

There was discussion in the video about user population and how many users could be accommodated by the linear transponders as well as the wideband digital channel. The number of people beneath the footprint of 4A and 4B for that matter is very large. The way that people will access the satellites is really unknown. 4A is making guesses and using previous experiences to try to make estimates, but it was emphasized that we just do not know how many people will use these satellites. Making very sure we have good gear and best operating practice is key. 

There will be a dedicated AMSAT earth station in Doha. There will be video transmitted on the uplink from Doha in order to test ATV reception, but at some point operators will uplink ATV. The decision to not have people connect to the earth station over the internet and then transmit ATV up to the satellite from there was discussed. The point of 4A is for operators to connect directly, learn DVB, and do it themselves. Peter Gulzow really wants the space symposium in two years to be directly transmitted through this satellite, and if all goes well, it will happen.  

Dish Donation! Some fun news here. There's a 5 meter dish that AMSAT is helping provide some 501c3 paperwork for. It's aluminum and beautiful. The surface is rated to 18 GHz.  Probably will work fine at 24 GHz. Made in Germany, shipped to Dallas, then not used. Very very thick rolled Aluminum. HEAVY! No mount. Big bucks to transport and mount. Chuck Clark AF8Z is interested. It would make one heck of a ground station.

Other things that need some time and attention are recruitment and solar power for Dixon Lake equipment and getting our website reviewed and published. 

I am back to jury duty tomorrow. Pick something and work hard! Try something new! Join ARRL, TAPR, or AMSAT or all three. If you know someone that would enjoy this project or might want to volunteer, then let them know. 

