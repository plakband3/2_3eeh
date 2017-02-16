from collections import Counter
from string import ascii_lowercase

with open('tekst.txt') as f:
    print (Counter(letter for line in f for letter in line.lower() if letter in ascii_lowercase))


#source used : http://stackoverflow.com/questions/18647707/count-letters-in-a-text-file