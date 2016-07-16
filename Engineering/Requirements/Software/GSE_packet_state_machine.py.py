#this is what was recommended by mossman
from bitstring import BitArray, BitStream

#A more OO way to handle this is to build a state machine using the state pattern.

#Handling incoming raw data is parsing where state machines provide an elegant solution 
#(you will have to choose between elegant and performance)

#You have a data buffer to process, each state has a handle buffer method that parses 
#and processes his part of the buffer (if already possible) and sets the next state based on the content.

#If you want to go for performance, you still can use a state machine, but leave out the OO part.







#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#snapshot of GSE_packet.py follows
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Baseband frame information
#should this be an object?
#N1 is the number of bytes until the end of the Base Band frame.
N1 = 10


#if start indicator == 0 and end indicator == 0 and label type indicator == 0
# then there are four padding bits, and padding bytes?


#Protocol Data Units are the things we want to encapsulate
#maybe these are a bitstream? Probably not? 
#How about making it a random value every time we run the code?

default_start = '0b1'
default_stop = '0b0'
default_label_type = '0b00'
#The GSE Label Field is optional. 
#Depending on the Label Type Indicator of the GSE Header, 
#the Label field can have a length of 6 byte, 3 byte or be omitted.
#00 6-byte label is present and shall be used for filtering
#01 3-byte label is present and shall be used for filtering
#10 Broadcast. No label field present. All Rx shall process this packet.
#   This combination shall be used also in non-broadcast systems when 
#   no filtering is applied at Layer 2, but IP header processing is utilized.
#11 Label re-use. No label field is present. All Rx shall reuse the label 
#   that was present in the previous Start or Complete GSE Packet of the 
#   same Base Band frame. This method is used for transmitting a sequence 
#   of GSE packets with the same label without repeating the label field. 
#   This value shall not be used for the first GSE packet in the frame. 

default_GSE_length = '0b101010101010'
#This 12-bit field indicates the length, in bytes, of the GSE Packet 
#counted from the byte following this GSE Length field. The GSE Length 
#field allows for a length of up to 4096 bytes for a GSE Packet. 
#The GSE Length field points to the start of the following GSE Packet, 
#or to the end of the Data Field or start of the padding field if the 
#GSE packet is the last in the frame.

default_fragment_ID = '0b01010101'
#This is present when a PDU fragment is included in the GSE Packet, 
#while it is not present if Start_Indicator and End_Indicator are 
#both set to "1". All GSE Packets containing PDU fragments belonging 
#to the same PDU shall contain the same Frag ID. The selected Frag ID 
#shall not be re-used on the link until the last fragment of the PDU 
#has been transmitted. (see clause 4.3).

default_total_length = '0b1110111011101110'
#This field is present in the GSE Header carrying the first fragment 
#of a fragmented PDU. The 16-bit field carries the value of the total 
#length, defined as the length, in bytes, of the Protocol Type, Label 
#(6 byte Label or 3 byte Label), Extension Headers, and the full PDU. 
#The receiver shall perform a total length check after reassembly. It
#may also use the total length information for pre-allocation of buffer 
#space. Although the length of a single GSE Packet
#is limited to almost 4 096 bytes, larger PDUs are supported through 
#fragmentation, up to a total length of 65,536 bytes.
#NOTE 2: Since the information in the total length field is intended 
#for use by higher layers in the reassembly process, the length of the 
#CRC_32 field is therefore not included in the Total_Length. 

default_protocol_type = '0b 1000 0110 1101 1101'
#This 16-bit field indicates the type of payload carried in the PDU, 
#or the presence of a Next-Header. The set of values that may be 
#assigned to this field is divided into two ranges, similar to the 
#allocation of Ethernet and shall follow the rules described in [5]. The two ranges are:
	#Type 1: Next-Header Type field 
	#Type 2: EtherType compatible Type Fields 
	#EXAMPLE: 0x0800: IPv4 payload
	 			#0x86DD: IPv6 payload 

#default_label presence and length depends on the label type
if default_label_type == '0b00':
	print "label type is 00 which is a six byte label"
	default_label = '0b101011010101010110101101010101011010110101010101'
elif default_label_type == '0b01':
	print "label type is 01 which is a three byte label"
	default_label = '0b101011010101010101010101'
elif default_label_type == '0b10':
	print "label type is 10 which is broadcast."
	default_label = None
elif default_label_type == '0b11':
	print "label type is 11 which is reuse last label."
	default_label = None
else:
	print "label type was unrecognized."
	default_label = None



#data_byte: These bytes shall contain a concatenation of any 
#extension header bytes, and the PDU data. The optional
#extension header bytes shall be used to carry one or more 
#extension header(s). The extension header format is defined 
#by the ULE specification [5]. For further details on this field, 
#also see clause 4.2.4.
#NOTE 3: N2 is the length of the encapsulated PDU or PDU fragment in bytes. 


zero_prefix = '0b00000'
H_LEN = '0b111'
#001 optional extension header length of 2 bytes
#010 optional extension header length of 4 bytes
#011 optional extension header length of 6 bytes
#100 optional extension header length of 8 bytes
#101 optional extension header length of 10 bytes
H_TYPE = '0b11111111'
#represents either one of 256 Mandatory Extension Headers or
#represents one of 256 Optional Extension Headers
default_extension_header_1 = zero_prefix+H_LEN+H_TYPE


#default_extension_header_2 =





#CRC_32: This field is only present in a GSE Packet that carries 
#the last PDU fragment. This field shall be set as defined in clause 4.2.2. 


class GSE:
	def __init__(self):
		start = BitArray(default_start)
		print "start is ", start
		stop = BitArray(default_stop)
		print "stop is ", stop
		label_type = BitArray(default_label_type)
		print "label type is", label_type



		#they have to exist before we can use them
		padding = BitArray()
		fragment_ID = BitArray()
		total_length = BitArray()	
		protocol_type = BitArray()	
		label = BitArray()


		
		if start == '0b0' and stop == '0b0' and label_type == '0b00':
			print "padding condition has been met"

#N1 is the number of bytes until the end of the Base Band frame.
#how do we get N1? Keep track of it with calculations?
			for x in range(0, N1-1):{
			padding.append('0b00000000')
			}
			
		
		GSE_length = BitArray(default_GSE_length)
		
		
		if start == '0b0' and stop == '0b0':
			fragment_ID = BitArray(default_fragment_ID)
			print "fragment ID condition has been met and fragment ID value is", fragment_ID
		
		if start == '0b1' and stop == '0b0':
			total_length = BitArray(default_total_length)
			print "total length field condition has been met and total length value is", total_length
		
		if start == '0b1':
			protocol_type = BitArray(default_protocol_type)
			print "protocol type field condition has been met and protocol type value is", protocol_type
			if label_type == '0b00':
				label = BitArray(default_label)
				print "six byte label condition has been met and the label is", label
			elif label_type == '0b01':
				label = BitArray(default_label)
				print "three byte label condition has been met and the label is", label


		fixed_header = start+stop+label_type+GSE_length

		self.data = fixed_header+padding+fragment_ID+total_length+protocol_type+label
		self.size = len(self.data)

#Encapsulated Packet Unit = GSE Packet
class EPU:
	def __init__(self):
		self.data = pack('!bb', 0xe, 0xf)
	

#Baseband frame
class BBF:
	def __init__(self):
		self.data = [0,0,0,0,0,0,0,0,0,0,0,0]
		#demo data [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]

#one of two topmost units that make GSE packets
class PDU_manager:
	def __init__(self):
		self.data = [0,0,0]
		#for example


	
		
#stores received PDU packets 
#Provides QoS and ACM support
#ACM FIFO queues
#three priority levels
#each priority level has a different ACM mode
class Scheduler_queue:
	def __init__(self):
		self.data = [0,0,0]
		#for example

class EF_queue:
	def __init__(self):
		self.data = [0,0,0]
		#for example
	
class AF_queue:
	def __init__(self):
		self.data = [0,0,0]
		#for example

	
class BE_queue:
	def __init__(self):
		self.data = [0,0,0]
		#for example
	
class ACM_updater:
	def __init__(self):
		self.data = [0,0,0]
		#for example
	
class Priority_solver:
	def __init__(self):
		self.data = [0,0,0]
		#for example

	
class Timeout_scheduler:
	def __init__(self):
		self.data = [0,0,0]
		#for example

	
class Priority_scheduler:
	def __init__(self):
		self.data = [0,0,0]
		#for example
		
		
		
		
		

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#one of two topmost units. EPU_manager Makes baseband frames.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#The PLHEADER is intended for receiver synchronization and physical layer signalling.

#Prior to modulation, each PLFRAME, excluding the PLHEADER, shall be randomized 
#for energy dispersal by multiplying the (I+jQ) samples by a complex randomization sequence (CI+jCQ):

#Two PLFRAME configurations shall be possible:
#• Without pilots.
#• With pilots.
#In this latter case a PILOT BLOCK shall be composed of P = 36 pilot symbols. 
#Each pilot shall be an un-modulated symbol, identified by I = (1/√2), Q = (1/√2). 
#The first PILOT BLOCK shall be inserted 16 SLOTs after the PLHEADER, the second 
#after 32 SLOTs and so on, as represented in figure 13. If the PILOT BLOCK 
#position coincides with the beginning of the next SOF, then the PILOT BLOCK is not transmitted.
#The pilot presence/absence in VCM and ACM can be changed on a frame-by-frame basis.

#NOTE: After decoding the PLHEADER, the receiver knows the PLFRAME duration and structure, 
#the modulation and coding scheme of the XFECFRAME, the presence or absence of pilot symbols.
#The PLHEADER (one SLOT of 90 symbols) shall be composed of the following fields:
#• SOF (26 symbols), identifying the Start of Frame.
#• PLS code (64 symbol): PLS (Physical Layer Signalling) code shall be a non-systematic 
#binary code of length 64 and dimension 7 with minimum distance dmin = 32. 
#It is equivalent to the first order Reed-Muller under permutation. 
#It transmits 7 bits for physical layer signalling purpose. 
#These 7 bits consists of two fields: MODCOD and TYPE defined as follows:
#- MODCOD (5 symbols), identifying the XFECFRAME modulation and FEC rate;
#- TYPE (2 symbols), identifying the FECFRAME length (64 800 bits or 16 200 bits) 
#and the presence/absence of pilots.
class EPU_manager:
	def __init__(self):
		#self.data = [0,0,0]
		#for example
	def produce_bbframe(self, trick):
	def produce_PLHEADER():
		#kick out a PLHEADER by itself
		
		
a = GSE()
print "GSE data is", a.data
print "GSE data size is", a.size