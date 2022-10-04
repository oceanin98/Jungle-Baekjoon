#차례대로 입력을 하고 마지막 부터 count해서 큰숫자 합 구하기
import sys
input=sys.stdin.readline
n=int(input())
stack=[]


for i in range(n):

    stack.append(int(input()))

right = int(stack[-1])
top = int(max(stack))
count = 1

while right != top:
    
    if len(stack)==0 or right == top:
        break
    
    if int(stack[-1]) <= right:#보이지 않으면 제거
        stack.pop()
        print(stack)
    elif int(stack[-1]) > right:#만약 막대기가 기준보다 크다면
        # print(stack)
        right= int(stack[-1])#기준으 바꾸고
        count +=1#더해준다
        stack.pop()
        
        
print(count)

