import random

n = int(input("Please input the length of poet : "))
for i in range(1, n + 1):
    num = random.randint(44032, 55215)
    print(chr(num), end="")
    if random.randint(1, 10) in range(1, 3):
        print()
    if random.randint(1, 10) in range(1, 5):
        print(" ", end="")
print()
