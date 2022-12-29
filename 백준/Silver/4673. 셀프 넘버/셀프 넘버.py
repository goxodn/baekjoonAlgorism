def func(num):
    list = [0 for index in range(num+50)]
    for index in range(num):
        castingNum = str(index)
        sum = 0
        for cas in range(len(castingNum)):
            sum = sum + int(castingNum[cas])
        sum = sum + index
        list[sum] = 1

    return list

list = func(10000)

for index in range(10000):
    if list[index] == 0 :
        print(index)
