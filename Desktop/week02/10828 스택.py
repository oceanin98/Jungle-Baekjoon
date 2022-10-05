
import sys

input=sys.stdin.readline

n= int(input())
stack=[]

for _ in range(n):
    word=input().split()
    order = word[0]

    if order =="push":
        value= word[1]
        stack.append(value)

    elif order=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    elif order=="size":
            print(len(stack))

    elif order =="empty":
        if len(stack) ==0:
            print(1)
        else:
            print(0)

    elif order== "top":
        if len(stack)==0:
            print(-1)

        else:
            print(stack[-1])
            
            
            
            

# class Stack:
#     def __init__(self):
#         self.stack =[]

#     def push(self, data):
#         self.stack.append(data)
    
#     def pop(self):
#         if self.empty():
#             return -1
#         else:
#             return self.stack.pop()

#     def size(self):
#         return len(self.stack)

#     def empty(self):
#         if len(self.stack) == 0:
#             return 1
#         else:
#             return 0

#     def top(self):
#         if self.empty():
#             return -1
#         else:
#             return self.stack[-1]


# N = int(input())
# S = []
# stack = Stack()
# result = 0
# for _ in range(N):
#     S.append(sys.stdin.readline().rsplit())
# for i in range(N):
#     if S[i][0] == "push":
#         stack.push(S[i][1])
#         continue
#     elif S[i][0] == "pop":
#         result = stack.pop()
#     elif S[i][0] == "size":
#         result = stack.size()
#     elif S[i][0] == "empty":
#         result = stack.empty()
#     elif S[i][0] == "top":
#         result = stack.top()
#     print(result)




