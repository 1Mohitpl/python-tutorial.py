import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_char = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+',
                '[',']','{','}','|',';',':',"'",'"',',','.','<','>','?','/','~']

# 🔹 Take input ONCE
s_letters = int(input("How many letters you want in your password? : "))
s_numbers = int(input("How many numbers you want in your password? : "))
s_special_char = int(input("How many special characters you want in your password? : "))

# 🔹 How many passwords to generate
total_passwords = int(input("How many passwords do you want to generate? : "))

print("\nGenerated Passwords 👇")

for _ in range(total_passwords):
    passwordList = []

    for i in range(s_letters):
        passwordList.append(random.choice(letters))

    for i in range(s_numbers):
        passwordList.append(random.choice(numbers))

    for i in range(s_special_char):
        passwordList.append(random.choice(special_char))

    random.shuffle(passwordList)

    # convert list to string
    password = ""
    for ch in passwordList:
        password += ch

    print(password)


