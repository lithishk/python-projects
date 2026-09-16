import random
import string
passwords=[]
def password_generator(letter,symbol, number):
    password = ""
    total_letters = list(string.ascii_letters)
    total_symbols = list(string.punctuation)
    total_numbers = list(string.digits)
    for i in range(letter):
        letters=random.choice(total_letters)
        password+=letters
    for i in range(symbol):
        symbols=random.choice(total_symbols)
        password+=symbols
    for i in range(number):
        numbers=random.choice(total_numbers)
        password+=numbers
    new_password=list(password)
    random.shuffle(new_password)
    password = "".join(new_password)
    passwords.append(password)
    return password


continue_generation='yes'
while continue_generation=="yes":
    while True:
        try:
            letter = int(input("Enter how many letters do you want: "))
            symbol = int(input("Enter how many symbols do you want: "))
            number = int(input("Enter how many numbers do you want: "))
            if letter==0 and number==0 and symbol==0:
                print("🙌🏻 At least one value must be greater than 0!")
                continue
            if letter<0 or number<0 or symbol<0:
                print("Please enter a positive number!")
                continue
            if letter>=10 or symbol>=10 or number>=10:
                print("It is too long!")
                continue
            break
        except ValueError:
            print("Please enter a number")
            continue


    new_password=password_generator(letter,symbol,number)

    print(f"Your password is: {new_password}")


    if (letter<3 and symbol<3 and number<3) or (len(new_password)<3):
        print("Strength: 🔴 Weak")
    elif (letter<6 and symbol<6 and number<6) or (len(new_password)<6):
        print("Strength: 🟠 Medium")
    else:
        print("Strength: 🟢 Strong")

    while True:
        continue_generation=input("Do you want to continue? (yes/no): ").lower()
        if continue_generation.isdigit():
            print("Enter (yes/no): ")
            continue
        break
if continue_generation=="no":
    os.system("cls")
    print(f"Password history: ")
    i = 0
    for password in passwords:
        i += 1
        print(i,'.', password)
    passwords.clear()
