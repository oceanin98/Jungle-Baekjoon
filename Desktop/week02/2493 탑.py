#차례대로 입력하고
#왼쪽부터 1 순서를 지정
#마지막부터 앞에 큰숫자의 순서를 출력
#앞에 큰숫자가 없으면0

import sys

n= int(sys.stdin.readline())
top= list(map(int,sys.stdin.readline().split()))
top= [[i+1,v] for i ,v in enumerate(top)]
#1부터 입력한 숫자와 같이 나옴
stack=[]

# print(top)
for s in top:
    
    while stack :
        if stack[-1][1] <= s[1]:
           stack.pop()
        else:
            print(stack[-1][0],end=' ')
            break   
        
             
    if not stack:
        print(0, end=' ')
    stack.append(s)
    
