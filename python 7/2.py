import random

def random_number():
    s1 = {random.randint(15, 45) for _ in range(10)}
    print(s1)
    a = 0
    for i in s1:
        if i < 30:
            a += 1
            print("that number is <30: ", i)
    print(a)
    s1_filtered = {i for i in s1 if i < 35}
    for i in s1:
        if i >= 35:
            print("removed number >=35: ", i)
    s1 = s1_filtered
    print(s1)

random_number()
