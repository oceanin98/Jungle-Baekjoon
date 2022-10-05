import sys
s,n = map(int,sys.stdin.readline().split())
nums = sys.stdin.readline().rstrip()
# nums = [[i+1,v] for i, v in enumerate(nums)]
stack=[]
# 앞뒤 비교해서 큰 숫자 result넣기
#비교할때 앞숫자와 result에 숫자 비교해서 크면 result 적으면 pop


for num in nums :
    while stack and stack[-1] < num and n >0:
        stack.pop()
        n -=1
    stack.append(num)

while n>0:
    min_mun=min(stack)
    stack.remove(min_mun)
    n -=1  
print('' .join(stack))
     