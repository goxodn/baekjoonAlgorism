num = int(input())

beeHouse = 1
increase = 0
root = 1
while num > beeHouse :
    increase = increase + 6
    root = root + 1
    beeHouse = beeHouse + increase

print(root)