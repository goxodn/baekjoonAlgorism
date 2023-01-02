phoneList = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
phoneNumber  = input()
outNumber = list()
sumNumber = 0
for i in range(len(phoneNumber)):
    for j in range(len(phoneList)):
        for k in range(len(phoneList[j])):
            if phoneNumber[i] == phoneList[j][k] :
                if j == 0 :
                    sumNumber = sumNumber + 3
                else :
                    sumNumber = sumNumber + j + 3
print(sumNumber)