#절대값이 비슷한 숫자 찾기
#부호가 다르면 뺴기 같으면 더하기
#비교해서 0에 가까운 숫자 두개 구하기 
import sys
input= sys.stdin.readline
n= int(input())
nums = sorted(list(map(int,input().split())))

nums.sort()

left = 0
right = n-1
ans= 10**10
idx=(0,0)

#왼쪽과 오른쪽이 달라
while left != right:
    #왼쪽과 오른쪽 더한거가 절대값크기가 ans보다 작아야해
    if ans > abs(nums[left]+ nums[right]):
        #ans는 맨 왼쪽과 오른쪽거 더하고 절대값 
        ans = abs(nums[left]+nums[right])
        idx = (left, right)
    
    if nums[left] + nums[right] < 0:
        left += 1
    elif nums[left] + nums[right] > 0:
        right -= 1
    else:
        break

print(nums[idx[0]], nums[idx[1]])