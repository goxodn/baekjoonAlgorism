numList = []

for i in range(5):
    numList.append(int(input()))

numList.sort()

print(sum(numList)//5)
print(numList[int(len(numList)/2)])
