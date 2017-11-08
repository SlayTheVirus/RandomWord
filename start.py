import random

words = [line.strip() for line in open('/src/wordlist.txt')]
print(random.choice(words))
