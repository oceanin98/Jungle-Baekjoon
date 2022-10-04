import sys
input=sys.stdin.readline

n,m= map(int,input().split())
tree= list(map(int,input().split()))

start=0
end=sum(tree)
#나무의 높이가 절단기 높이보다 크다면 
#자르기
#자른 나무들의 길이가 목표값보다 크다면

while start<= end:
    mid = (start+end)//2
    t=1 #잘린 나무

    for i in tree:
        if i> mid: 
            t += i - mid #중간보다 큰값 자름

    if t>m:
        start = mid +1 #원하는 나 높이보다 더  많이 잘ㅏ으면
    else: #원하는 나무 높이보다 덜 잘렸으면 
        end=mid  -1
print(end)


