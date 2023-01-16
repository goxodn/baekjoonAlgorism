def insertionSort(data):
    for i in range(0,len(data),1):
        for j in range(i,0,-1):
            if data[j] > data[j-1]:
                data[j] , data[j-1] = data[j-1] , data[j]
            else :
                break
    return list

groupWord = input()
list = list()
for i in range(len(groupWord)):
    list.append(int(groupWord[i]))

list2 = insertionSort(list)
for i in list2:
    print(i , end='')