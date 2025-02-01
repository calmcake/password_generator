from random import choice, randint, shuffle
import string

def generate_password(length, spec_char, upper_letters, numbers):
    
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов")
    
    password_char_list = []
    
    spec_char_list = list(string.punctuation)
    upper_letters_list = list(string.ascii_uppercase)
    lower_letters_list = list(string.ascii_lowercase)
    numbers_list = list(string.digits)

    if spec_char:
        random_number = randint(1, 2)
        length -= random_number
        
        for i in range(random_number):
            password_char_list.append(choice(spec_char_list))
        
    if upper_letters:
        random_number = randint(1, 2)
        length -= random_number
        
        for i in range(random_number):
            password_char_list.append(choice(upper_letters_list))

    if numbers:
        random_number = randint(1, 2)
        length -= random_number
        
        for i in range(random_number):
            password_char_list.append(choice(numbers_list))
        
    for i in range(length):
        password_char_list.append(choice(lower_letters_list))
    shuffle(password_char_list)
    return ''.join(password_char_list)


def choose_parameters():
    while True:
        try:
            length = int(input("Number of characters (min 4) - "))
            if length < 4:
                print("Password length must be at least 4. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")

    spec_char = input("Are special characters needed? (y/n) - ").lower() == "y"
    upper_letters = input("Are capital letters needed? (y/n) - ").lower() == "y"
    numbers = input("Are numbers needed? (y/n) - ").lower() == "y"
    
    return length, spec_char, upper_letters, numbers


print("Welcome to the password generator")
print("You can customize your password. You can add special characters, capital letters and numbers")

parameters = choose_parameters()

length = parameters[0]
spec_char = parameters[1]
upper_letters = parameters[2]
numbers = parameters[3]

password = generate_password(length, spec_char, upper_letters, numbers)

print("\n✅ Your generated password:")
print("=" * (len(password) + 4))
print(f"🔒 {password} 🔒")
print("=" * (len(password) + 4))
