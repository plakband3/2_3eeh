from collections import Counter
from string import ascii_lowercase
p = open("coded.txt", "w")
with open('tekst.txt') as f:
    print (Counter(letter for line in f for letter in line.lower() if letter in ascii_lowercase))

with open("tekst.txt") as coded:

    for line in coded:
        for ch in line:
            if ch in ascii_lowercase:
                oldChar = (ord(ch))
                newChar = oldChar + 5;
                if newChar > 122:
                    newChar -= 26

                print (chr(newChar))




                p.write(chr(newChar))













#source used : http://stackoverflow.com/questions/18647707/count-letters-in-a-text-file