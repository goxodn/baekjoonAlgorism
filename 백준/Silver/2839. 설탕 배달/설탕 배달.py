N = int(input())

start = N//5
output = -1
for a in range(start,-1,-1):
    if (N-5*a)%3 == 0:
        output = a + (N-5*a)//3
        break

print(output)