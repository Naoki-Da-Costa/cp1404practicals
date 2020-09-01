import random


number_of_quick_picks = int(input("How many quick picks: "))
for i in range(number_of_quick_picks):
    quick_picks = []
    for i in range(6):
        quick_pick_values = random.randint(1, 45)
        while quick_pick_values in quick_picks:
            quick_pick_values = random.randint(1, 45)
        quick_picks.append(quick_pick_values)
    quick_picks.sort()
    print(" ".join("{:2}".format(quick_pick_values) for quick_pick_values in quick_picks))
