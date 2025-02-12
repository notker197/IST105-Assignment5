import sys
import math
import random

# Obtener los datos del formulario
number = int(sys.argv[1])
text = sys.argv[2]

# Tarea 1: Número Puzzle
if number % 2 == 0:
    result_number = f"The number {number} is even. Its square root is {math.sqrt(number):.2f}."
else:
    result_number = f"The number {number} is odd. Its cube is {number ** 3}."

# Tarea 2: Texto Puzzle
binary_text = ' '.join(format(ord(char), '08b') for char in text)
vowel_count = sum(1 for char in text if char.lower() in 'aeiou')

# Tarea 3: Treasure Hunt
secret_number = random.randint(1, 100)
attempts = 0
guessed = False

while attempts < 5 and not guessed:
    attempts += 1
    guess = random.randint(1, 100)  # Simulación de intento del usuario
    if guess == secret_number:
        guessed = True

if guessed:
    treasure_result = f"You found the treasure in {attempts} attempts!"
else:
    treasure_result = "You did not find the treasure within 5 attempts."

# Imprimir resultados
print(f"Number Puzzle:\n{result_number}\n")
print(f"Text Puzzle:\nBinary: {binary_text}\nVowel Count: {vowel_count}\n")
print(f"Treasure Hunt:\n{treasure_result}")