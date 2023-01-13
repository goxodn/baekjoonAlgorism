def star(n):
    arr = []
    if n == 1:
        arr.append('*')
    else:
        val = star(n//3)

        for v in val:
            arr.append(v*3)
        for v in val:
            arr.append(v+' '*(n//3)+v)
        for v in val:
            arr.append(v*3)

    return arr

N = int(input())
print('\n'.join(star(N)))
