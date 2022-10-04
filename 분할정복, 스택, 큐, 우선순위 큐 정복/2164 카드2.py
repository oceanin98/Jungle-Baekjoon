#1번이 제일 위 n이 제일 아래
#제일 위를 버리고 그다음 카드는 제일 아래로 옮긴다
#n개가 주어졌을때 제일 마지막에 남은 카드는?

import sys
input= sys.stdin.readlines
from collections import deque



#n을 while로 1 부터 n+1까지
#정렬해서 앞에 pop하고 다음은 맨뒤로 보내기 반복
#popleft사용

n= int(input())
deque= deque([ i for i in range(1,n+1)])

 
while (len (deque)>1):
    deque.popleft()
    move_num= deque.popleft()
    deque.append(move_num)
    

