a,b = map(int,input().split())

list = list(map(int,input().split()))

maxNum = 0

for firstCard in range(len(list)):
    for secondCard in range(1,len(list)-1):
        for thirdCard in range(2,len(list)-2):
            if firstCard == secondCard or firstCard == thirdCard or secondCard == thirdCard :
                pass
            elif list[firstCard] + list[secondCard] + list[thirdCard] <= b and list[firstCard] + list[secondCard] + list[thirdCard] >= maxNum :
                maxNum =  list[firstCard] + list[secondCard] + list[thirdCard]

print(maxNum)