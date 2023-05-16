from string import ascii_uppercase
from random import randint
from time import sleep

naturals = ascii_uppercase[:7]
musical_alphabet = []
for letter in naturals:
    if letter == 'B' or letter == 'E':
        musical_alphabet.append(f"{letter}b")
        musical_alphabet.append(letter)
    elif letter == 'C' or letter == 'F':
        musical_alphabet.append(letter)
        musical_alphabet.append(f"{letter}#")
    else:
        musical_alphabet.append(f"{letter}b")
        musical_alphabet.append(letter)
        musical_alphabet.append(f"{letter}#")

print()
speed = int(input("How long do you want to wait before the next note?:"))
sleep(2)
while True:
    i = randint(0, len(musical_alphabet) - 1)
    print(f"Play {musical_alphabet[i]}")
    sleep(speed)
