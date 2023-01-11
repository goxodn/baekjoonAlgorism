N = int(input())
M = int(input())
A = []
for i in range(N,M+1):
    cnt = 0
    for j in range(2, i+1) :
        if i%j == 0 :
            cnt += 1
    if cnt == 1:
        A.append(i)
if len(A) == 0 :
    print(-1)
else :
    print(sum(A))
    print(min(A))