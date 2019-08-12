import random

quick_pick = int(input("How many quick picks to generate"))
for i in range(quick_pick):
    quick_picks = []
    for j in range(6):
        number = random.randint(1,45)
        while(number in quick_picks):
            number = random.randint(1,45)
        quick_picks.append(number)
    quick_picks.sort()
    for num in quick_picks:
        print("{:2}".format(num), end =' ')
    print()

