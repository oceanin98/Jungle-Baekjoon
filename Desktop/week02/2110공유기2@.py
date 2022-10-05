import sys

n , c = map(int,sys.stdin.readline().split())
houses=[]

for _ in range(n):
    houses.append(int(sys.stdin.readline()))
    
    #이분탐색을 위해 정렬
houses.sort()
# print(houses)
#최소거리와 최대거리를 포인터로 설정
left_pointer =1 #최소 거리는 좌표값이 연속된 숫자인 경우이므로 1
right_pointer = houses[-1] - houses[0]#최대거리는 맨끝집과 맨 앞집 사이의 거리
answer =0

#이분 검색 시작
while left_pointer <= right_pointer:
    #공유기 설치 인접 거리를 중앙값과 비교하며 검색
    middle = (left_pointer + right_pointer)//2
    
    #첫 번째 집에 공유기를 설치하고 시작
    c=1
    before_house= houses[0]
    #검색시작
    for i in range(1, len(houses)):
        if houses[i] - before_house >= middle:
            c+=1
            before_house= houses[i]
    #주어진 공유기 개수보다 적다면 범위를 줄여 middle 값 줄이기
    if c<c:
        right_pointer = middle +1
    #그렇지 않고 더 많은 공유기를 설치했다면 범위를 늘려 middle값 늘리기
    else:
        left_pointer = middle +1
    #middle 값을 저장해주는 이유는 조건에 충족해서 범위를 늘리거나 줄였을때
    #반복문이 break 될수 있으므로 가장 최근의 가능했던 값을 저장
    answer= middle
print(answer)
            