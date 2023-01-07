highScore = 0
locationX = 0
locationY = 0
list = [
    9 * [0] for index in range(9)
]
for i in range(9):
    N = input().split()
    for j in range(9):
        list[i][j] = N[j]

for i in range(9):
    for j in range(9):
        if int(list[i][j]) >= int(highScore) :
            highScore = list[i][j]
            locationX  = i
            locationY = j
print(highScore)
print(locationX+1,locationY+1)