ALPHABET_SIZE = 26

message: str = input("Message: ")  
key: int = int(input("Key: "))

ciphertext: str = ""

#Encription massage:

for character in message:  
    if "A" <= character <= "Z":
        shifted = ord(character) + key  
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)
    else: 
        ciphertext += character

print ("Ciphertext:", ciphertext)

plaintext: str = ""

#Decription massage:
for character in ciphertext:  
    if "A" <= character <= "Z":
        shifted = ord(character) - key  
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)
    else:
        plaintext += character

print ("Plaintext:", plaintext)

assert plaintext == message

