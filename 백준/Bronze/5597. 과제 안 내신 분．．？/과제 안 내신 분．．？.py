studentList = [0 for i in range(30)]

"""학생이 각각 제출을 하는 부분"""
for index in range(28):
    studentNum = int(input())
    studentList[studentNum-1] = 1

"""학생이 제출을 하지 않았을 경우"""
for index in range(len(studentList)):
    if studentList[index] == 0:
        print(index+1)
