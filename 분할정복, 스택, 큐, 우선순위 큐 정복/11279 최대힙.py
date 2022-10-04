#n을 입력하고 
#아래로 x를 입력
#0개수만큼 출력
#하나씩 stack에 넣는데 큰수 앞에 
#0이 나올떄마다 앞에수 pop
#stack이 비어있을경우 0 출력


import readline
import sys
import heapq

input= sys.stdin.readline

n= int(input())
heap =[]
for _ in range(n):
    num=int(input())
    if not num:
        if heap:
            print((heapq.heappop(heap)))
        else:
            print(0)
    else:
        heapq.heappush(heap,num)