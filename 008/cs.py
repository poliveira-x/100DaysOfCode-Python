# Caesar Cipher
#

# put the alphabet into a string
letters =""
for i in range(97, 97+26):
    letters += chr(i)


# get a message to be encrypted and
#turn it in lower case
message = input("Message: ").lower()

# get the encryptkey
key = int(input("Type the key: "))


# look for the letters and change
# them using the key do that for
# the whole message change only letters.

encrypt_msg = ""
for i in message:
    for j in range(26):
        if i == letters[j]:
            if j+key > 25:
                x = j+key - 26
                encrypt_msg += letters[x]
            else:
                encrypt_msg += letters[j+key]




print(encrypt_msg)




