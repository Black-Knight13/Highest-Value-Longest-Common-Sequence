# Generates data for test cases
import os
import string 
import random

# creates list from a-z
alphabet = list(string.ascii_lowercase)

#assigns values to each letter
values = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

# list of sizes for test cases
sizes = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]

# generates test cases and writes them to files in tests directory
os.makedirs("tests", exist_ok=True)
for idx, n in enumerate(sizes):
    A = "".join(random.choices(alphabet, k=n))
    B = "".join(random.choices(alphabet, k=n))
    with open(os.path.join("tests", f"test{idx+1}.in"), "w") as f:
        f.write(f"{len(alphabet)}\n")
        for char in alphabet:
            f.write(f"{char} {values[char]}\n")
        f.write(f"{A}\n")
        f.write(f"{B}\n")
print ("Data generation complete!")