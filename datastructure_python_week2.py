# 2.1 구구단 6단을 계산하여 결과를 순서대로 출력하는 코드를 for문을 이용하여 구현하라.

from random import randrange, uniform
import string
from tempfile import tempdir
from turtle import up


def gugudan(n):
    for i in range(1,10):
        print(n * i)
# 2.2 위 문제를 while문을 이용하여 다시 구현하라
def gugudan2(n):
    i = 1
    while i < 10:
        print(n * i)
        i += 1

#2.3 구구단 6단을 계산 결과를 역순으로 출력하는 코드를 for와 range를 이용하여 구현하라
def gugudan3(n):
    for i in range(9 , 0 , -1):
        print( n * i )


#2.4 섭씨온도를 화씨 온도로 변환하는 함수를 구현하라. 섭씨온두('C)를 화씨온도('F)로 변환하는 수식은 F = 32 + 180/100 * C이다.

def transTemperature(C):
    F = 32 + 180/100 * C
    print(F)

# 2.5 화씨온도를 섭씨온도로 변환하는 함수를 구현하라.

def transTemperature2(F):
    C = (F - 32) / (180/100)
    print(C)

# 2.6 A = [1,2,3,4]와 같이 리스트를 선언하고 이 리스트의 모든 값이 역순으로 출력하는 코드를 구현하라. 단, 인덱스 값으로는 음수만을 사용하라.
def revList(A : list):
    for i in range(-1 ,  -(len(A)+1) , -1):
        print(A[i])

#2.7 리스트의 모든 값을 더해 겨로가를 반환하는 함수를 구현하라.
def sumList(A : list):
    sum = 0
    for i in range(0 , len(A)):
        sum += A[i]
    
    return sum


# 2.8 문자열 msg = "Data Structure in Python"를 선언하고, 이 문자열을 먼저 그래도 출력하고,
# 다음으로 모두 대문자로 바꿔서 출력하고, 마지막으로 모두 소문자로 바꿔 출력하는 코드를 작성하라.

def upperStr(msg):
    msg = msg.upper()
    return msg

def lowerStr(msg):
    msg = msg.lower()
    return msg

def printStr(msg):
    print(msg)

# 2.9 어느 식당의 음식에 대한 가격 정보를 다음과 같이 딕셔너리로 표현하자.
# price = {'콩나물해장국' : 4500, '갈비탕' : 9000, '돈가스' : 8000}
# 여기에 새로운 메뉴 '팟타이'를 7000원에 추가하고, 모든 메뉴와 가격을 출력하는 코드를 작성해보라.

def addMenu(price , menuName, menuPrice):
    price[menuName] = menuPrice
    print(price)

# 2.10 위 문제에서 모든 메뉴와 가격을 500원 내리는 코드를 작성해보자.

def downAllPrice(price , downPrice):
    for i in price:
        price[i] -= 500
    
    return price



# 2.11 1부터 n 까지의 숫자를 전부 합하여 반환하는 순환적인 함수를 작성하라.
def sumNumbers(n , sum = 0):
    if n > 0:
        sum += n
        return sumNumbers(n-1 , sum)
    else:
        return sum

# 2.12 다음을 계산하는 순환적인 함수를 작성하라.
# 1 + 1/2 + 1/3 + .... + 1/n

def sumHarmonicSeries(n , sum = 0):
    if n > 0:
        sum += 1/n
        return sumHarmonicSeries(n -1 , sum)
    else:
        return sum

# 2.13 이항계수(binomial coefficient)를 계산하는 순환함수를 작성하라. 이항계수는 다음과 같이 순환적으로 정의 된다.
#n_C_k = n-1_C_k-1 + n-1_C_k if 0< k < n
#      = 1 if k = 0 or k = n


        
def cal_binomialCoefficient(n,k):
    
    if k == 0 or k ==n:
        return 1
    return cal_binomialCoefficient(n-1 , k - 1 ) + cal_binomialCoefficient(n-1 , k)


# 2.14 이항계수를 구하는 함수를 반복 구조로 구현하라

def factorial(n):
    value = 1
    for i in range(1,n+1):
        value *= i
    return value

def cal_binomicalCoeffincient2(n,k):
    return factorial(n) // (factorial(k) * factorial(n-k))

# 2.15 문자열의 내용을 반대로 바꾸는 순환적인 함수 reverse()를 구현하라.
# 예를 들어 reverse("ABCDE") 는 "EDCBA"를 반환해야한다.

def reverse(str : string):
    revStr =""
    for i in range(1,len(str)+1):
        revStr += str[-i]
        
    return revStr

# 2.16 순환을 사용하여 1부터 n 까지의 숫자를 화면에 순서대로 출력하는 함수 printNum(n)과
# 역순으로 출력하는 함수 printRevNum(n)을 작성하라.
# 다음은 각각 printNum(10)과 printRevNum(10)의 출력 결과이다.

# 1 2 3 4 5 6 7 8 9 10
# 10 9 8 7 6 5 4 3 2 1

def printNum(n):
    for i in range(1,n+1):
        print(i, end = " ")

def printRevNum(n : int):
    for i in range(n ,0 , -1):
        print(i, end = " ")

# 2.17 순환적인 방법으로 피보나치 수열을 호출하였을 때 함수가 중복되어 호출되는 것을
# 확인할 수 있도록 각 함수의 매개 변수별 호출 빈도를 측정해 출력하라



def fibo( n, temp):
    temp[n] += 1
    if n < 2:
        return n
    return fibo(n-1,temp) + fibo(n-2,temp)

# n = 7

# temp = dict()
# for i in range(0, n +1 ):
#     temp[i] = 0

# fibo(7,temp)
# for i in range(0 , n+1):
#     print(f"Fibo({i}) = {temp[i]}번")

# ****************실습문제*****************************

# 2.2 번호 맞히기 게임을 구현하자. 숨겨진 두자리의 숫자를 추측하여 맞추는 것이다.
# 게이머가 숫자를 예측하면 컴퓨터는 정답을 비교하여 

# "더 큰 숫자입니다." 나 "더작은 숫자입니다." 그리고 맞힌 경우 "정답입니다."를 출력한다.
# 중간에 맞히거나 10번 동안 맞히지 못하면 게임이 끝난다.

# 정답을 answer 추츩 문자를 guess라 하면, answer와 huess를 비교하여 결과를 출력하면 된다.
# 정답 범위를 힌트로 제공하기 위해 min과 max변수를 사용한다.

# 반복문으로는 for를 사용하고 최대 10번 반복하면서, 중간에 정답을 맞히면 break문을 이용해 루프를 빠져나와 게임을 종료한다.



def upAndDownGame(n):
    numRange = [0, 100]
    for i in range(0, 10):
        
        print(f"숫자를 입력하세요.(범위:{numRange[0]} ~ {numRange[1]}) : " , end = " ")
        a = int(input())
        if a == n :
            print(f"정답입니다. {i+1}번 만에 맞추셨습니다.")
            print("게임이 끝났습니다.")
            break
        elif a < n:
            print("아닙니다. 더 큰 숫자입니다.")
            numRange[0] = a
        else:
            print("아닙니다. 더 작은 숫자입니다.")
            numRange[1] = a

import os
n = randrange(100)

while(True):
    upAndDownGame(n)
    os.system("pause")
