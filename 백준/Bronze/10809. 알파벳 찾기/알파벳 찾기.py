"""

word = input()

wordList = [-1 for index in range(127)]
for index in range(len(word)):
    if wordList[ord(word[index])] < 0 :
        wordList[ord(word[index])] = index

print(wordList[97:123])

"""

word = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for index in alphabet:
    if index in word :
        print(word.find(index) , end=' ')
    else:
        print(-1 , end= ' ')