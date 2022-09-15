# 2.1 구구단 6단을 계산하여 결과를 순서대로 출력하는 코드를 for문을 이용하여 구현하라.

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