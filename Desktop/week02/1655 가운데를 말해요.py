#일단 입력
#stack에 넣기 들어가면 정렬해서 중간숫자 나오게 하기?
#중간값보다 작은 값들은 leftheap 크면 right
#


from multiprocessing import heap
import sys
import heapq

input = sys.stdin.readline

n= int(input())
#여기에 인제 왼오 순서로 넣을 공간
leftheap=[]
rightheap=[]


for _ in range(n):
    num = int(input())
    

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -num)
    else:
        heapq.heappush(rightheap,num)
#왼 오를 비교하는거지
    if rightheap and rightheap[0]< -leftheap[0]:
#
        leftvalue = heapq.heappop(leftheap)
        rightvalue= heapq.heappop(rightheap)
        
        heapq.heappush(leftheap, -rightvalue)
        heapq.heappush(rightheap, -leftvalue)
    
    print(-leftheap[0])
    
    
        
        
    