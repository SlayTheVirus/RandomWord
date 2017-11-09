import random
import time

while True:
    words = [line.strip() for line in open('wordlist.txt')]
    print(random.choice(words))
    time.sleep(5)
