sum = 0
totalPrice = int(input())
choice = int(input())

for index in range(choice):
    a,b = map(int,input().split())
    sum = sum + (a * b)
    
if sum == totalPrice :
    print("Yes")
else :
    print("No")
    
    
    