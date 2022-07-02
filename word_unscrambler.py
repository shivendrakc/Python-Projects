from itertools import permutations
import enchant

d = enchant.Dict("en_US")

op = set()
word = input("Enter your letters :")
letter = [x.lower() for x in word]

for n in range(3, len(word)):
    for y in list(permutations(letter, n)):
        z = "".join(y)
        if d.check(z):
            op.add(z)
    
print(op)