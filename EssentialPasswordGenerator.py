import random
import string

def generate_password(length, num_range, letter_range):
    num_start, num_end = num_range
    letter_start, letter_end = letter_range

    if length < 2:
        return "Password length must be at least 2 characters."

    # Generate the numbers part
    numbers = [str(random.randint(num_start, num_end)) for _ in range(length // 3)]

    # Generate the letters part
    letters = [chr(random.randint(ord(letter_start), ord(letter_end))) for _ in range(length // 3)]

    # Generate the mixed case letters part
    mixed_letters = [chr(random.randint(ord('a'), ord('z'))) for _ in range(length - len(numbers) - len(letters))]
    mixed_letters = [random.choice([str.upper, str.lower])(char) for char in mixed_letters]

    # Combine numbers, letters, and mixed case letters
    password = ''.join (random.sample(''.join(numbers + letters + mixed_letters), length))

    return password

# Ask the user how many passwords to generate
num_passwords = int(input("How many passwords would you like to generate? "))

# Ask for the password length
password_length = int(input("Password length: "))

# Ask for the number range
num_start = int(input("Starting value of the number range: "))
num_end = int(input("Ending value of the number range: "))

# Ask for the letter range
letter_start = input("Starting letter of the letter range: ")
letter_end = input("Ending letter of the letter range: ")

passwords = []

for _ in range(num_passwords):
    num_range = (num_start, num_end)
    letter_range = (letter_start, letter_end)
    password = generate_password(password_length, num_range, letter_range)
    passwords.append(password)

# Print the generated passwords
print(f"Generated password list:")
for password in passwords:
    print(password)
