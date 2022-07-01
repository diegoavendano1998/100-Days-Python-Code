import string
import random

# Todas las letras ascii mayusculas y minusculas
alphabet_string = list(string.ascii_lowercase+string.ascii_uppercase)
numbers = list(range(0,10))
symbols = ["!","#","$","&","*","+"]
num_letters = int(input("How many letters do you want in the password? "))
num_numbers = int(input("How many numbers do you want in the password? "))
num_symbols = int(input("How many symbols do you want in the password? "))
total_characters = num_letters+num_numbers+num_symbols
password = []
for i in range(0,total_characters):
    password.append(random.choice(alphabet_string))
for i in range(0,num_numbers):
    index = random.randint(0,total_characters-1)
    if password[index] in alphabet_string:
        password[index] = str(random.choice(numbers))
    else:
        b = False
        for i in range(0,total_characters):
            if password[i] in alphabet_string and not b:
                password[i] = str(random.choice(numbers))
                b = True
for i in range(0,num_symbols):
    index = random.randint(0,total_characters-1)
    if password[index] in alphabet_string:
        password[index] = str(random.choice(symbols))
    else:
        b = False
        for i in range(0,total_characters):
            if password[i] in alphabet_string and not b:
                password[i] = str(random.choice(symbols))
                b = True
password_string = ""
for character in password:
    password_string += character
print(f"Your new password is {password_string}")


# Una manera mas facil es user random.shuffle():
# password = []
# for i in range(0,num_letters):
#     password.append(random.choice(alphabet_string))
# for i in range(0,num_numbers):
#     password.append(random.choice(numbers))
# for i in range(0,num_symbols):
#     password.append(random.choice(symbols))
# random.shuffle(password)
# password_string = ""
# for character in password:
#     password_string += character
# print(f"Your new password is {password_string}")

