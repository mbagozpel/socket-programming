
# The 64-bit key is permutted according to the following table
key_drop = (
	57, 49, 41, 33, 25, 17,  9,
	 1, 58, 50, 42, 34, 26, 18,
	10,  2, 59, 51, 43, 35, 27,
	19, 11,  3, 60, 52, 44, 36,
	63, 55, 47, 39, 31, 23, 15,
	 7, 62, 54, 46, 38, 30, 22,
	14,  6, 61, 53, 45, 37, 29,
	21, 13,  5, 28, 20, 12,  4)

compression_table = (    
	14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
	)

#Initial Permutation Table

initial_permutation = (
	58, 50, 42, 34, 26, 18, 10, 2,
	60, 52, 44, 36, 28, 20, 12, 4,
	62, 54, 46, 38, 30, 22, 14, 6,
	64, 56, 48, 40, 32, 24, 16, 8,
	57, 49, 41, 33, 25, 17,  9, 1,
	59, 51, 43, 35, 27, 19, 11, 3,
	61, 53, 45, 37, 29, 21, 13, 5,
	63, 55, 47, 39, 31, 23, 15, 7
	)

#Expansion Bit Selection Table
Exp_table = (
	32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
    )

 #Substitution boxes
S_boxes = {
	0: (
        14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
        0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
        4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
        15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
    ),
    1: (
        15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
        3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
        0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
        13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9 
    ),
    2: (
        10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
        13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
        13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
        1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12 
    ),
    3: (
        7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
        13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
        10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
        3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
    ),
    4: (
        2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
        14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
        4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
        11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
    ),
    5: (
        12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
        9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
        4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
    ),
    6:(
        4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
        13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
        1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
        6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
    ),
    7: (
        13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
        1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
        7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
        2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
    )}

#32-bit Output Permutation table
perm_table = (
    16,  7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11, 4,  25
)

#Final Permutation Table
final_permutation = (
	40, 8, 48, 16, 56, 24, 64, 32,
	39, 7, 47, 15, 55, 23, 63, 31,
	38, 6, 46, 14, 54, 22, 62, 30,
	37, 5, 45, 13, 53, 21, 61, 29,
	36, 4, 44, 12, 52, 20, 60, 28,
	35, 3, 43, 11, 51, 19, 59, 27,
	34, 2, 42, 10, 50, 18, 58, 26,
	33, 1, 41, 	9, 49, 17, 57, 25,
	)

#permute function to rearrange the bits
def permute(block, block_len, table):
	#convert and return the binary string equivalent of the block
	bin_str = bin(block)[2:].zfill(block_len)
	permutation = []
	for i in range(len(table)):
		permutation.append(bin_str[table[i] - 1])
	return int(''.join(permutation), 2)

#Function to generate round keys
def generate_round_keys(lpt, rpt):
	#returns a dictionary of 16 keys (one for each round)

	round_keys = dict.fromkeys(range(0,17))
	left_shift_values = (1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1)

	#left-rotation function
	left_shift = lambda pt, r_bits, max_bits: \
	(pt << r_bits%max_bits) & (2**max_bits-1) | \
	((pt & (2**max_bits-1)) >> (max_bits - (r_bits % max_bits)))

	#initial rotation
	lpt = left_shift(lpt, 0, 28)
	rpt = left_shift(rpt, 0, 28)
	round_keys[0] = (lpt, rpt)

	#create 16 more different key pairs
	for index, val in enumerate(left_shift_values):
		index += 1
		lpt_index = left_shift(round_keys[index -1][0], val, 28)
		rpt_index = left_shift(round_keys[index - 1][1], val, 28)
		round_keys[index] = (lpt_index, rpt_index)


	#del round_keys[0]
	del round_keys[0]

	#finally, for the keys form concatenated lpt_i and rpt_i
	for i, (lpt_index, rpt_index) in round_keys.items():
		Ci = (lpt_index << 28) + rpt_index
		#convert from 56-bit to 48-bit
		round_keys[i] = permute(Ci, 56, compression_table)
	return round_keys

#Function that expands a blockfrom 32-bit to 48-bit using the Expansion table
def expansion_function(block_i, round_key):
	# expand block_1 from 32 go 48 bit 
	block_i = permute(block_i, 32, Exp_table)

	#xor with round key
	block_i ^= round_key

	#split block_1 into 8 groups of 6-bits
	block_i_blocks = [((block_i & (0b111111 << shift_val)) >> shift_val) for shift_val in (42,36,30,24,18,12,6,0)]

	#interpret each block as address for the S-boxes
	for i, block in enumerate(block_i_blocks):
		#grab the bits we need
		row = ((0b100000 & block) >> 4) + (0b1 & block)
		col = (0b011110 & block) >> 1
		#sboxes are stored as one-dimensional tuple, so we need to calc the index this way
		block_i_blocks[1] = S_boxes[i][16* row + col]

	#pack the blocks together again by concatenating
	block_i_blocks = zip(block_i_blocks, (28, 24, 20, 16, 12, 8, 4, 0))
	block_i = 0
	for block, lshift_value in block_i_blocks:
		block_i += (block << lshift_value)

	#another permutation 32bit -> 32bit
	block_i = permute(block_i, 32, perm_table)

	return block_i

def encrypt(message, key, decrypt = False) :
	# Encrypt single blocks only
	assert isinstance(message, int) and isinstance(key, int)
	assert not message.bit_length() > 64
	assert not key.bit_length() > 64

	#Convert from 64-bit to 56-bit
	key = permute(key, 64, key_drop) 

	#split up key into two halves
	# generate the 16 round keys
	lpt = key >> 28
	rpt = key & (2**28-1)
	#convert from 56-bit to 64-bit
	round_keys = generate_round_keys(lpt, rpt) 

	message_block = permute(message, 64, initial_permutation)
	print(f'After initial permutation: {message_block}' )
	Left = message_block >> 32
	Right = message_block & (2**32-1)

	#apply the round function 16 times
	Left_last = Left
	Right_last = Right

	

	for i in range(1,17):
		if decrypt: #Use the round keys in reversed order
			i = 17 - i
		Left_round = Right_last
		Right_round = Left_last ^ expansion_function(Right_last, round_keys[i])
		Left_last = Left_round
		Right_last = Right_round
		print(f'Round {i + 1}: " " {Left_last}, " " {Right_last}')

	# concatenate reversed
	combine = (Right_round << 32) + Left_round

	#final permutation
	cipher_text = permute(combine, 64, final_permutation)

	return cipher_text

def test_result(key, message):
	print('****Encryption....****')
	cipher_text = (encrypt(message, key))
	print('\n')
	print('......................................')
	print('\n')
	print(f'(Encrypted: {cipher_text}')
	print('\n')
	print('......................................')
	print('\n')
	print('****Decryption***')

	plain_text = hex(encrypt(cipher_text, key, decrypt = True))
	print('\n')
	print('......................................')
	print('\n')
	print(f'Decrypted: {plain_text}')

k = 0x133457799BBCDFF1
m =  0x0123456789ABCDEF

	
test_result(k, m)


