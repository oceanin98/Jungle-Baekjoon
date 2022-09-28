import math #수학 관련 함수를 사용할수 있다 (사인,코사인,제곱근 등 )
a,b,v= map(int,input().split())
day= math.ceil((v-a)/(a-b))+1 #ceil함수는 소수 올림 내릴려면 floor

print(day)
