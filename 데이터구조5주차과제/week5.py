from sys import displayhook


class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):return len(self.top)==0
    def size(self):return len(self.top)
    def clear(self): self.top=[]

    def push(self,item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            
            return

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            
            return


    def display(self, temp = []):
        if self.isEmpty():
            return
        temp.append(self.pop())
        print(temp[-1])
        
        return self.display()


# values=Stack()
# for i in range(20):
#     if i%3 == 0:
#         print(f"i%3 = {i%3} , {i}")
#         values.push(i)
#     elif i%4 ==0:
#         print(i%4, i)
#         values.pop()


def revStr(A):
    A = list(A)
    for i in range(0,len(A)):
        print(A.pop(), end = '')

def revStrWithStk(A):
    stk =Stack()
    for i in A:
        stk.push(i)
    while not stk.isEmpty():
        print(stk.pop(), end='')

# A = 'Hello World'
# revStr(A)
# print()
# revStrWithStk(A)


# 2. 4.3절의 괄호 검사 프로그램을 다음과 같이 확장하세요.
# 1) 소스 파일을 읽어 괄호를 검사하는 프로그램을 완성하세요. 임의의 파일을 입력하면 괄호를 검사한다.
# 2) 괄호 매칭이 실패하면 조건 1~3중 어떤 조건을 위반했는지 출력하도록 소스를 수정하세요. 이때 checkBrackets() 함수가 에러코드를 반환하도록 한다. (0이면 정상, 1~3 에러번호)
# 3) 괄호 매칭이 실패하면 실패한 위치(줄번호, 문자위치)를 에러코드와 함께 출력하도록 한다. 이를 위해 checkBrackes()함수는 (에러코드, 줄번호, 문자위치)를 반환하도록 한다. 


filename = "C:\새파일.txt"

infile = open(filename, "w")
infile.write('(((())))()()()[][[]](')
infile = open(filename, "r")
lines = infile.readlines();


def checkBracketV2(lines):
    stack = Stack()
    i = 1
    for line in lines:
        
        print(line)
        j = 1
        for ch in line:
            if ch in ('{', '[', '('):
                j +=1
                stack.push(ch)
            elif ch in ('}', ']', ')'):
                j +=1
                if stack.isEmpty():
                    print(f"error 2 {i}번째 줄입니다. {j}번째 자리입니다.")
                    return
                else:
                    left = stack.pop()
                    if (ch == "}") and left != "{" or  (ch == "]") and left != "[" or  (ch == ")") and left != "(":
                        print(f"error 3 {i}번째 줄입니다.{j}번째 자리입니다.")
                        return
            j +=1
            
        i+=1
    if stack.isEmpty():
        print("0")
        return
    else:
        print(f"error 1 {i}번째 줄 {j}번째 자리입니다.")
        return

result = checkBracketV2(lines)

infile.close()