import random
import string

# Define a function to generate a random alphanumeric or special character
def generate_random_char():
    characters = string.ascii_letters + string.digits + string.punctuation
    return random.choice(characters)

# Generate associated characters for digits 0 to 9
associated_chars = {}

for digit in range(10):
    chars = [generate_random_char() for _ in range(4)]
    associated_chars[str(digit)] = chars

# Define the phone keypad layout
keypad_layout = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

# Print the associated characters below each number
for row in keypad_layout:
    for digit in row:
        chars = associated_chars.get(digit, [' '] * 4)
        print(f"  {digit}", end='\t')
    print()
    for digit in row:
        chars = associated_chars.get(digit, [' '] * 4)
        print(''.join(chars), end='\t')
    print()
