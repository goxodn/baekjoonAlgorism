개수 = int(input())

for _ in range(개수):
    층 = int(input())
    호 = int(input())
    아파트 = [x for x in range(1, 호+1)]
    for k in range(층):
        for i in range(1, 호):
            아파트[i] += 아파트[i-1]
    print(아파트[-1])