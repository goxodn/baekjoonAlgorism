숫자 = int(input())
숫자리스트 = map(int, input().split())
소수 = 0
for num in 숫자리스트:
    에러 = 0
    if num > 1 :
        for i in range(2, num): 
            if num % i == 0:
                에러 += 1
        if 에러 == 0:
            소수 += 1
print(소수)