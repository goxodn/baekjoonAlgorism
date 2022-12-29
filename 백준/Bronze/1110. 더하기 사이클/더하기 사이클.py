def func(num):
    firstNum = int(num/10)
    secondNum = int(num%10)
    thirdNum = 0
    fourthNum = 0

    sum = firstNum + secondNum

    if(sum >= 10):
        fourthNum = sum % 10
    else :
        fourthNum = sum

    thirdNum = secondNum * 10
    sum = thirdNum + fourthNum

    return sum

num = int(input())
result = num
count = 0

while True :
    count = count + 1
    result = func(result)
    if num == result:
        break

print(count)