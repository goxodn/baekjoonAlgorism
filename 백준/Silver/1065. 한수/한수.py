n = int(input())
num = 0

if(n<100):
    num = n
else:
    num = 99
    for index in range(100,n+1,1) :
        parseNum = str(index)
        calone = int(parseNum[1])-int(parseNum[0])
        caltwo = int(parseNum[2])-int(parseNum[1])

        if calone == caltwo :
            num = num + 1
print(num)

