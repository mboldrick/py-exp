"""
Read a file and display its contents.
"""
import re
from pathlib import Path

path = Path('data/pi_million_digits.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
birthday_loc_find = pi_string.find(birthday)
if birthday_loc_find > -1:
    print(f"Your birthday appears in the first million digits of pi starting at position {birthday_loc_find}.")
else:
    print("Your birthday does NOT appear in the first million digits of pi.")

# use regex to search for birthday.
match = re.search(birthday, pi_string)
if match is not None:
    print(f"Your birthday appears in the first million digits of pi starting at position {match.start()}.")
else:
    print("Your birthday does NOT appear in the first million digits of pi.")

# use regex to search for all occurrences of birthday.
match = re.findall(birthday, pi_string)
print(len(match))
if len(match) > 0:
    print(f"Your birthday appears in the first million digits of pi {len(match)} times,"
          f" starting at position {match.start()}.")
else:
    print("Your birthday does NOT appear in the first million digits of pi.")

# use standard list, but the position is not given.
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does NOT appear in the first million digits of pi.")

# print(f"{pi_string[:52]}...")
# print(len(pi_string))
# print(contents)
