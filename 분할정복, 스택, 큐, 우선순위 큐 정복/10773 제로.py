#숫자0일떄마자 바로 뒤에있는 값이 없어짐
n= int(input())

z=[]

for i in range(n):
    num= int(input())
    if num == 0:
        z.pop
    else:
        z.append(num)
print(sum(z))