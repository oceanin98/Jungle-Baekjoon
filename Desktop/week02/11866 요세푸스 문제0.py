# 1번부터 n번까지
#k번째를 제거하고 반복


#k-1만큼 빼고 더하고를 반복
#k숫자번 빼기 
#출력할때 괄호 형식

from collections import deque


result=[]
dequeA=deque()

n,k= map(int,input().split())
for i in range(1, n+1):
    dequeA.append(i)
    

while dequeA:
    for i in range(k-1):
        dequeA.append(dequeA.popleft())
    result.append(dequeA.popleft())


print("<",end='')
for i in range(len(result)-1):
    #하나씩 출력됨
    print("%d, "%result[i], end='')
print(result[-1], end='')
print(">")

