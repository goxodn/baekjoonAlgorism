def recursion(s, l, r, c):
    if l >= r:
        re = '1' + ' ' + str(c+1)
        return re
    elif s[l] != s[r]:
        re = '0' + ' ' + str(c+1)
        return re
    else:
        return recursion(s, l + 1, r - 1, c + 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 0)


"s = abc l = 0 r = 2 0,1,2 "

N = int(input())

for i in range(N):
    print(isPalindrome(input()))
