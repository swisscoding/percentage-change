#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

import colored

# decoration
print(colored.stylize("\n---- | Calculate percentage change of share value | ----\n", colored.fg("red")))

share_count = int(input("How much shares do you want to calculate?\n"))
print()

# [[share, old_price, current_price], ...]
shares = []

print("Input your share/s in this form ->\nshare_name old_price current_price <enter>\nPrices in US Dollar ($)\n")
for _ in range(share_count):
    shares += [[ i for i in input(": ").split() ]]

print(colored.stylize("\n----------------", colored.fg("sandy_brown")))

def percentage_change(list):
    for i in list:
        if float(i[1]) > float(i[2]):
            decrease = 100 - 100/float(i[1])*float(i[2])
            shares[shares.index(i)].append(colored.stylize(f"Decrease: {round(decrease, 1)}%", colored.fg("red")))
        elif float(i[1]) < float(i[2]):
            increase = 100/float(i[1])*float(i[2]) - 100
            shares[shares.index(i)].append(colored.stylize(f"Increase: {round(increase, 1)}%", colored.fg("green")))
        else:
            return 0
    return shares

def show(list):
    if list == 0:
        print("\nNo in- or decrease of your share/s.\n")
    else:
        for i in list:
            print(f"\nShare name: {i[0]}\nOld price: {i[1]}$\nCurrent price: {i[2]}$\n{i[3]}")
        print()

show(percentage_change(shares))
