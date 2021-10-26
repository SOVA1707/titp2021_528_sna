import random

def func(length, min, max):
    n = []
    i = 0
    while i<length:
        n.append(round(random.uniform(min, max), 2))
        i = i+1
    return n

n = func(5, -40, 100)
print(n)
sum = 0
for i in n:
    if i>0: sum = sum + i
print(sum)
