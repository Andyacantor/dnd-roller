import random


def roll_dice():
    x = random.randint(1, 20)

    print("Let's roll some frelling dice!")
    print(x)

    if x <= 10:
        print("Low number!")

    else:
        print("High number!")


roll_dice()
