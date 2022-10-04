from sys import stdin
input= stdin.readline

#n개의 집에 c개의 공유기를 설치해야한다
#가장 인접한 공유기 사이의 거리가 최대가 되도록 해야한다

n,c= map(int,input().split())
a=[int(input()) for _ in range(n)]

#시작은 최소거리 끝은 최대거리
def binary_search(a):
    left, right =1, a[-1]- a[0]
    
    
    while left <= right:
        mid= (left+right)//2
        cur=a[0]
        cnt=1
    #앞집부터 공유기 설치 
        for i in range(1, len(a)):
            if a[i] - cur >= mid:
                cur = a[i]
            cnt += 1
    #설치할수 있는 공유기가 c개를 넘어가면  다시 앞집부터 설치
        if cnt >= c:
            left= mid +1
        else:
    #넘어가지 않으면 더 좁게 설치
            right = mid -1
        
        
    return right

print(binary_search(sorted(a)))


