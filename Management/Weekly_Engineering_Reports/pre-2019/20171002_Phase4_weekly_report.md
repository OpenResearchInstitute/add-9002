Greetings!

Today we're talking about our simplified pi/2 BPSK decoder, working under the assumption that symbol timing and phase have already been resolved to a single sample per symbol.

This work fits into the much larger picture of acquiring phase, timing of symbols, demodulation, decoding, and correlation to the fixed patterns of the Start of Frame field in the physical layer header that helps define each DVB-S2 frame.

The DVB-S2 physical layer header is sent using a modulation scheme called pi/2 BPSK. This scheme is defined in the standard. Since we're using GNU Radio as our reference design, we decided to make a custom block in GNU Radio to do this. This block will evolve to include our specific type of correlation for the Start of Frame as well. 

Given that we needed a block, we had to learn how to make one. 

There is a very useful GNU Radio Block Coding Style Guide here. https://wiki.gnuradio.org/index.php/BlocksCodingGuide

There is a helpful set of guided tutorials on the GNU Radio website here. https://wiki.gnuradio.org/index.php/Guided_Tutorials

A block in GNU Radio is the unit of signal processing from which you build a flow graph. It can implement a very simple function or it can be very complex, and it might or might not take parameters that control how it works. Related blocks are grouped into a “module”. The name of the module shows up in GNU Radio Companion as the category header for blocks that belong to the module.

To help build blocks and modules, there's a tool built in to GNU Radio called gr-modtool. One of its functions is that it sets up a module. Another function lets you add blocks to that module.

Using gr-modtool is relatively easy. It sets up the right directory structure for you and it provides templates in either python or c++ for the implementation of your block. I'm not going to duplicate the tutorial here. Find this specific tutorial here https://wiki.gnuradio.org/index.php/Guided_Tutorial_GNU_Radio_in_C%2B%2B

If you walk through this tutorial you will be well on your way to being able to code GNU Radio blocks. 

After doing the tutorial a couple of times, we attacked the problem of demodulating pi/2 BPSK. 

We started with the definition in the spec.

"SOF shall correspond to the sequence 18D2E82HEX (01-1000-....-0010 in binary notation, the left-side bit being the MSB of the PLHEADER)" 90 degree BPSK, so in complex notation, it's…

"The PLHEADER, represented by the binary sequence (y1, y2,...y90) shall be modulated into 90 π/2BPSK symbols according to the rule:
 I sub 2i-1 = Q sub 2i-1 = (1/√2) (1-2y sub 2i-1), I sub 2i = - Q sub 2i = - (1/√2) (1-2y sub 2i) for i = 1, 2, ..., 45 "

If we think of I and Q as coordinates in a cartesian plane, we have what's called a constellation diagram. Using this visualization, in pi/2 BPSK the information is encoded as the direction of rotation around the unit circle: clockwise 90 degrees (pi/2 radians) for a 1 or counterclockwise by the same amount for a 0, with each received symbol. Because the next stage of the receive pipeline is a correlator, we choose to output +1.0 for a clockwise rotation and -1.0 for a counterclockwise rotation. This encoding will be helpful later, when we change to a more sophisticated demodulator implementation.

The signal never stays in the same quadrant for two symbols, nor does it ever cross through the center by moving 180 degrees at once. If we see either sequence in the received symbol stream, we know it is an error. We pass that information along to the next stage as what's called an erasure, encoded as a value of 0.0.

This really needs to be reviewed to make sure we have interpreted it correctly. Code for this block can be found at the following repository and discussed in the code review channel in Slack. https://github.com/phase4ground/correlator

Once we thought we understood the way pi/2 BPSK worked, we wrote quality assurance test code. The gr-modtool sets up unit testing templates for you, so that you can test first like highly evolved and successful programmers always do.*

Then we wrote some demodulation code. It didn't work. We wrote more. It didn't work either. QA tests kept failing. We went back to the drawing board and realized that it would never work. We proved that the problem couldn't be simplified combinatorially. We then wrote a table lookup for the combinations of previous and current symbols. Here's the table we started with and went back to. Because we assume the symbols are already symchronized and lined up for us, we only need to pay attention to the sign bit of each sample.

I_previous	Q_previous	I_current	Q_current	Result
+		+		+		+		erasure
+		+		+		-		clockwise
+		+		-		+		counterclockwise
+		+		-		-		erasure
+		-		+		+		counterclockwise
+		-		+		-		erasure
+		-		-		+		erasure
+		-		-		-		clockwise
-		+		+		+		clockwise
-		+		+		-		erasure
-		+		-		+		erasure
-		+		-		-		counterclockwise
-		-		+		+		erasure
-		-		+		-		counterclockwise
-		-		-		+		clockwise
-		-		-		-		erasure


We receive a series of complex signal snapshots. We establish a history, where we tell GNU radio that we need to keep track of the most recently received complex signal along with the current one. This means we use the set_history function in the constructor. The history value is 2. We need the previous signal in order to tell which direction the signal moved and whether or not that move was valid. 

In our complex signal world, the previous result and the current result are each composed of a real and imaginary part, representing the in-phase or I and quadrature or Q components of the signal. Each part is a float.

The lookup is achieved by taking the signs of previous I, previous Q, current I, current Q with the signbit macro, and converting those sign bit results into an integer by multiplying each one by place values 8, 4, 2, and 1. The std::signbit() macro returns 0 for positive value and non-zero for negative values, so we use an old C programmer's trick to convert it into boolean 0 or 1 by negating it twice (!! “double bang”).

int tesla = (!!std::signbit(previous_input.real()))*8 + (!!std::signbit(previous_input.imag()))*4 + (!!std::signbit(current_input.real()))*2 + (!!std::signbit(current_input.imag()));
	
out[i] = mega[tesla];

Output is a table lookup.

mega is a list of floats constructed as follows.

float mega[] = {0.0, 1.0, -1.0, 0.0, -1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, -1.0, 0.0, -1.0, 1.0, 0.0};

The index created by the integer value tesla (binary coded number derived from the sign bits of the previous and current complex samples) will give the correct output value that corresponds to that combination of previous and current complex signal inputs.

A GNU Radio block is given a certain number of samples to work on each time its “work” function is called. That's no problem for operations that look at just one sample at a time, but we need to look at both the current sample and one previous sample. So how do we ever manage to handle the first sample that's passed into the work function? GNU Radio has a solution for this, called “history”. We call the set_history function and tell it the number of adjacent samples we need to examine, in this case 2. GNU Radio then arranges that each work buffer contains the extra previous sample that we need, in addition to all the new samples. Once we figured that out, and got the table indexing right, the simple unit test case we'd constructed finally passed.

Assuming that the demodulation is correct, the next step from here is to take our start of frame and look for received patterns that match it. When this happens, we will produce a tag. Tags in GNU Radio are synchronized chunks of information that are attached to samples. It is like metadata that can be used by other blocks. For this block, we are going to follow the conventions in the general correlation estimation block. This means that there will be several tags that can be used by downstream blocks that need them. Those downstream blocks have already implemented functions that consume the tags, so if we produce them, it makes for more useful flow graphs. 