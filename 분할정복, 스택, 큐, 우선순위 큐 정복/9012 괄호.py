#push=( pop =) 총 0 이되면 yes 안에 남아있으면 no
import sys

n=int(sys.stdin.readline())

for _ in range(n):
    #stack []여기에 하나씩 들어가기
    stack =[]
    # s는 괄호
    s= sys.stdin.readline().rstrip()
    #false 로시작
    flag=False
    #하나씩 들어가서 확인
    for i in s:
        #맞으면 stack에 i가 들어간다
        if i == '(':
            stack.append(i)
        else:
            #안에 ( 가있다면 꺼내
            if stack and stack[-1] == '(':
                stack.pop()
            else:
            #없으면 true하고 멈춤
                flag= True
                break
#만약에 stack에 들어있으면 no, 안에 )라서 falg=true가 된다면 no
    if stack or flag:
        print("NO")
    else:
        print("YES")
