import random
p  = int(input("How many letters would you like in your password?\n"))
q  = int(input("How many symbols would you like?\n"))
r = int(input("How many numbers would you like?\n"))

letters = ['A','B','C','D','E','F','G','H','J','K','L','M','N']
number = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','*','&','(',')']

password = ""

for char in range(1,p + 1):
    random_char = random.choice(letters)
    password += random_char
for char in range(1, q + 1):
    password += random.choice(number)
for char in range(1, r + 1):
    password += random.choice(symbols)
print(password)

password_list = []

for char in range(1,p + 1):
    password_list.append(random.choice(letters))
for char in range(1, q + 1):
    password_list.append(random.choice(number))
for char in range(1, r + 1):
    password_list.append(random.choice(symbols))

password = ""
for char in password_list:
   password += char
print(f"Your password is: {password}")
