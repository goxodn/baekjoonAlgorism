repeat_num = int(input())

stack = []
result = []
count = 1

for i in range(repeat_num):
    user_number = int(input())
    
    while count <= user_number:
        stack.append(count)
        result.append('+')
        count = count + 1
    
    if stack[-1] == user_number :
        del stack[-1]
        result.append('-')
    else :
        print('NO')
        exit(0)

print('\n' .join(result))