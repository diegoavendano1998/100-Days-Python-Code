from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(shift,text):
    new_word = ""
    for letter in text:
        index = alphabet.index(letter)
        alphabet_len = len(alphabet)-1
        if alphabet_len-index >= shift:
            new_letter = alphabet[index+shift]
        else:
            new_letter = alphabet[(shift-(alphabet_len-index))-1]
        new_word += new_letter
    print("The encoded word is: "+new_word)

def decrypt(shift,text):
    new_word = ""
    for letter in text:
        index = alphabet.index(letter)
        alphabet_len = len(alphabet)-1
        if index-shift >= 0:
            new_letter = alphabet[index-shift]
        else:
            new_letter = alphabet[(alphabet_len+(index-shift))+1]
        new_word += new_letter
    print("The decoded word is: "+new_word)


print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\t")
text = input("Type your message:\t").lower()
shift = int(input("Type the shift number:\t"))%26
if direction == "encode":
    encrypt(shift,text)
elif direction == "decode":
    decrypt(shift,text)
else:
    print("Invalid option. Bye ;)")

