def func(list):
    sum = 0
    copyList = []
    for i in range(1,len(list)+1,1):
        copyList.append(list[-i])
    b = "".join(copyList)
    return b

a,b = input().split()
if int(func(a)) >= int(func(b)):
    print(int(func(a)))
else :
    print(int(func(b)))
