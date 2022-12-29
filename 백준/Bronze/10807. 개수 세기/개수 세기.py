choice = int(input())

list = list(map(int,input().split()))
count = 0
checkNum = int(input())

for index in range(len(list)):
    if checkNum == list[index]:
        count = count + 1

print(count)