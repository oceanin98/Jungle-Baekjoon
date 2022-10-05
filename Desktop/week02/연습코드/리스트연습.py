
# n=[[1, 6], [2, 9], [3, 5], [4, 7], [5, 4]]
# print(n[-1][0])
# print(n[0])
# print(n[-1])

# import random

# a = []
# for i in range(100):
#     rnum = random.randint(1, 1000)
#     a.append(rnum)
# print(a)

import sys
input= sys.stdin.readline
n= int(input())



nums = list(map(int,input().split()))

while True:
    b = []
    if nums == "0":
        break


    for i in nums:
        tmp = abs(i-n)
        b.append(tmp)

    b.sort()
    search_val = b[0]
    
    for i in nums:
        tmp = abs(i-n)
        if tmp == search_val:
            print(i)
            break

