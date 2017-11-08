import random

words = [line.strip() for line in open('/src/')]
print(random.choice(words))
