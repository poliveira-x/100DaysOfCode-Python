# Caesar Cipher
#

def encrypt(msg, key, letters):
    encrypt_msg = ""
    for i in message:
        if i not in letters:
            encrypt_msg += i
        for j in range(26):
            if i == letters[j]:
                if j+key > 25:
                    x = j+key - 26
                    encrypt_msg += letters[x]
                else:
                    encrypt_msg += letters[j+key]

    return(encrypt_msg)


def decrypt(msg, key, letters):
    decrypt_msg = ""
    for i in message:
        if i not in letters:
            decrypt_msg += i
        for j in range(26):
            if i == letters[j]:
                if j-key < 0:
                    x = j-key + 26
                    decrypt_msg += letters[x]
                else:
                    decrypt_msg += letters[j-key]

    return(decrypt_msg)


letters =""
for i in range(97, 97+26):
    letters += chr(i)

opt = input("\n(E)ncript or (D)ecript: ")[0].lower()

message = input("Message: ").lower()

key = int(input("Type the key: "))

if opt == 'd':
    print(decrypt(message, key, letters))
elif opt == 'e':
    print(encrypt(message, key, letters))

