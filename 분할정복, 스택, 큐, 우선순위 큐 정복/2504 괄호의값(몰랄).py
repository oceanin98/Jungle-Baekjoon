
import sys

n=sys.stdin.readline().strip()
stack=[]
ans=0
#
for i in n:
    #만약에 ) 이거야
    if i ==')':
        #처음 닫는거면 t사용
        t = 0
        #안에 이미 있다면 꺼냄
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                #t==0이라면 2 넣기 인데 앞이 ( 라서 () 이 닫으니까 2
                if t ==0:
                    stack.append(2)
                else:
                    stack.append(2*t)
                break
            #만약에 (]이렇게 된다면 0출력
            elif top == '[':
                print(0)
                exit(0)
            # ([()])이런식이다 그러면..
            else:
                t += int(top)
    #)아니고 만약에 ]야            
    elif i ==']':
        #그러면 일단 t=0이야
        t=0
        while len(stack) != 0: #스택에 1개 이상이 있어!
            top = stack.pop() #앞에 있는걸 지워
            if top =='[': #방금 사라진 top이 [였다면 
                if t ==0: #그리고 t가 0이라면 
                    stack.append(3)#3을 넣어 
                else:
                    stack.append(3*t)
                break
            elif top == '(': #방금 들어온게 ]였는데 앞에가 (였다? 그럼 0
                print(0)
                exit(0)
            else:
                t += int(top) #방금 지운 숫자를 티에 저장
    #또 아니고 ( ,[ 라면 stack에 i를 넣는다
    else: 
        stack.append(i)
   
for s in stack:
    if s == '(' or s == '[':
        print(0)
        exit(0)
    else:
        ans += s
print(ans) 