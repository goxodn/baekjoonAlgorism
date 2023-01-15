def groupWordCheck(data):
    list = []
    for index in range(len(data)):
        if data[index] not in list :
            list.append(data[index])
        else :
            if data[index-1] == data[index] :
                list.append(data[index])
            else :
                return 0
    return 1

num = int(input())
count = 0

for i in range(num):
    groupWord = input()
    count = count + int(groupWordCheck(groupWord))

print(count)
