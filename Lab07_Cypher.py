# CS 161P // PYTHON // SUSAN EVANS
# LAB 7 // SUBSTITUTION CYPHER
# CREATED BY frankylee kelly.


# SUBSTITUTION CYPHER //
# Write a function that implements a substitution cypher. One letter should be substituted for another to garble the
# message. For example: A > Q; B > T; C > G; etc.
#
# Your function should take two parameters —— the message you want to encrypt and a string that represents the mapping
# of the 26 letters in the alphabet. Your function should return a string that is the encrypted version of the message.
#
# EXTENSIONS //
# Create a new function to decrypt the original message. It will have the encrypted string and mapping as parameters.


# GLOBAL VARIABLES // ALPHABET MAPPING
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CYPHER = "TVUSMEBNOIQKALXDGYFRWHZCJP"


# ENCRYPTION / DECRYPTION FUNCTION
def encryption(string, currentMap, changeMap):
	# VARIABLES
	translated = ''  # houses each char through encryption / decryption process

	# SWAP EACH LETTER IN STRING + MATCH CASE
	for letter in string:
		if letter.upper() in currentMap:
			char = currentMap.find(letter.upper())
			if letter.isupper():
				translated += changeMap[char].upper()
			else:
				translated += changeMap[char].lower()
		else:
			translated += letter

	# RETURN NEW MESSAGE
	return translated


# GET MESSAGE TO ENCRYPT
message = input("What message would you like to encrypt?  ")
print()  # spacer between collection + output

# CALL ENCRYPTION FUNCTION + PRINT
encryptMessage = encryption(message, ALPHABET, CYPHER)
print("Encrypted: {}".format(encryptMessage))

# CALL DECRYPTION + PRINT
decryptedMessage = encryption(encryptMessage, CYPHER, ALPHABET)
print("Decrypted: {}".format(decryptedMessage))

