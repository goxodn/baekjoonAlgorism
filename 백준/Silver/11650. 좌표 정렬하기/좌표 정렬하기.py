
num = int(input())

xySpace = []

#해당 x,y분면에 값 추가
for i in range(num):
    xy = list(map(int,input().split()))
    xySpace.append(xy)

xySpace.sort(reverse=False)

for i in xySpace :
    print(i[0],i[1])