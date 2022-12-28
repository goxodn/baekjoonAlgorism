num1 = int(input())
num2 = input()

num3 = int(num2[-1])*num1
num4 = int(num2[1])*num1
num5 = int(num2[0])*num1

print(num3)
print(num4)
print(num5)

num4 = num4*10
num5 = num5*100
print(num3+num4+num5)