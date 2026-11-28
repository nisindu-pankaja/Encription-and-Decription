ALPHABET_SIZE: int = 26

message: str = input("Message: ")
key: int = int(input("Key: "))

ciphertext: str = ""
for character in message:
    if "A" <= character <= "Z": #capital letters
        shifted: int = ord(character) + key
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)
    elif "a" <= character <= "z": #simple letters
            shifted: int = ord(character) + key
            if shifted > ord("z"):
                shifted -= ALPHABET_SIZE
            ciphertext += chr(shifted)
    else:
        ciphertext += character

print("Ciphertext:", ciphertext)

plaintext: str = ""
for character in ciphertext:
    if "A" <= character <= "Z": #capital letters
        shifted = ord(character) - key
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)
    elif "a" <= character <= "z": #simple letters
            shifted = ord(character) - key
            if shifted < ord("a"):
                shifted += ALPHABET_SIZE
            plaintext += chr(shifted)
    else:
        plaintext += character

print("Plaintext:", plaintext)

assert plaintext == message