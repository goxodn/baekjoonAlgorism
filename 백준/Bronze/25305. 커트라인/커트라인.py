N,K = map(int,input().split())
studentList = list(map(int,input().split()))
studentList.sort(reverse=True)
print(studentList[K-1])