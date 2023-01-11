num = int(input())
i = 1
if num <= 1:
    print()
else :
    while num >= 2 :
        i = i + 1
        if num % i == 0:
            print(i)
            num = num / i
            i = 1
        elif num == i :
            print(-1)
            break