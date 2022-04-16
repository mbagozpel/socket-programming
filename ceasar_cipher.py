
# Implementing Caesar Cipher algorithm using python in sublime text editor
# Define the encryption algorithm
''' STEPS:
	1. Loop through the plain text
	2. Use the ord() and chr() function to encrypt uppercase and lowercase characters in plain text.
		The ord() converts a character to its numeric representation in unicode, while
		the chr() function converts from numeric code to character'''

def encryption_algorithm(plaintext, shift_pattern):
	encryption = ''
	#Loop through the plain text
	for i in range(len(plaintext)):
		single_char = plaintext[i]

		#Using the ord() and chr() function to encrypt uppercase characters in plaintext
		if (single_char.isupper()):
			
			#check for the position unicode
			single_char_position = ord(single_char) - ord('A')
			#shift the current character by shift_pattern
			single_char_shifted = (single_char_position + shift_pattern) % 26 + ord('A')

			encryption += chr(single_char_shifted)

		#for lowercase
		elif (single_char.islower()):
			#check for poistion in unicode
			single_char_position = ord(single_char) - ord('a')
			#shift the current character
			single_char_shifted = (single_char_position + shift_pattern) % 26 + ord('a')

			encryption += chr(single_char_shifted)

		elif (single_char.isdigit()):
			#if it's a number, shift its actual value
			encryption += str(int(single_char) + shift_pattern) % 10

		else:
			#if its neither alphabetical nor a number, just leave it like that
			encryption += single_char

	return encryption

	# The Decryption Algorithm
def decryption_algorithm(ciphertext, shift_pattern):
		decryption = ''
		#Loop through ciphertext
		for i in range(len(ciphertext)):
			single_char = ciphertext[i]

			if single_char.isupper():
				#get the position
				single_char_position = ord(single_char) - ord('A')
				#shift the current character to the left by shift_pattern to get its original character
				single_char_shifted = (single_char_position - shift_pattern) % 26 + ord('A')

				decryption += chr(single_char_shifted)

			elif single_char.islower():
				#get the position in unicode
				single_char_position = ord(single_char) - ord('a')
				#shift the current character to the left shift_pattern to get its original character
				single_char_shifted = (single_char_position - shift_pattern) % 26 + ord('a')

				decryption += chr(single_char_shifted)

			elif single_char.isdigit():
				#if it's a number, shift its actual value
				decryption += str(int(single_char) - shift_pattern) % 10

			else:
				decryption += single_char

		return decryption

	#The Hacking algorithm

		
#Implementing the caesar function
plaintext = 'My name is Inie'
shift_pattern = 2
ciphertext = encryption_algorithm(plaintext, shift_pattern)
decrypted = decryption_algorithm(ciphertext, shift_pattern)
hacked = hack_caesar_cipher(ciphertext)

# print(f"Plain Text: {plaintext}")
# print(f"\nCipher Text: {ciphertext}")
# print(f"\nDecrypted Text: {decrypted}")


def hack_caesar_cipher(ciphertext):
		
		UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		lowercase = 'abcdefghijklmnopqrstuvwxyz'

				#Loop through alphabets
		for key in range(len(UPPERCASE)):
			hacked = ''
					#loop through ciphertext
			for i in ciphertext:
				if i in UPPERCASE:
					index = UPPERCASE.find(i)
					index = index - key
					if index < 0:
						index = index + len(UPPERCASE)
						#add number's symbol at the end of hacked
					hacked = hacked + UPPERCASE[index]
				elif i in lowercase:
					index = lowercase.find(i)
					index -= key
					if index < 0:
						index = index + len(lowercase)
					hacked = hacked + lowercase[index]
				else:
					hacked = hacked + i
			print(f'Key #{key}: {hacked}')

print(hack_caesar_cipher(ciphertext))




