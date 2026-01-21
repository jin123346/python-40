#부울 자료형

a = True
b = False
print("a:", a)  # 출력: a: True
print("b:", b)  # 출력: b: False
#출력 결과
# a: True
# b: False
#부울 연산자 예제
x = 10
y = 5
is_greater = x > y
is_equal = x == y
print("x가 y보다 큰가?:", is_greater)  # 출력: x가 y보다 큰가?: True
print("x와 y가 같은가?:", is_equal)     # 출력: x와 y가 같은가?: False
#출력 결과
# x가 y보다 큰가?: True
# x와 y가 같은가?: False
#부울 연산자 활용 예제  
a = 8
b = 12
result = (a < 10) and (b > 10)
print("a는 10보다 작고 b는 10보다 큰가?:", result)  # 출력: a는 10보다 작고 b는 10보다 큰가?: True
result = (a > 10) or (b > 10)       
print("a는 10보다 크거나 b는 10보다 큰가?:", result)  # 출력: a는 10보다 크거나 b는 10보다 큰가?: True
#출력 결과
# a는 10보다 작고 b는 10보다 큰가?: True
# a는 10보다 크거나 b는 10보다 큰가?: True
#부울 값 변환 예제
value1 = 0
value2 = "Hello"
bool1 = bool(value1)
bool2 = bool(value2)
print("value1의 부울 값:", bool1)  # 출력: value1의 부울 값: False
print("value2의 부울 값:", bool2)  # 출력: value2의 부울 값: True
#출력 결과
# value1의 부울 값: False   
# value2의 부울 값: True
#부울 값 활용 조건문 예제
is_raining = True   
if is_raining:
    print("우산을 챙기세요!")  # 출력: 우산을 챙기세요!
else:
    print("좋은 날씨입니다!")
#출력 결과
# 우산을 챙기세요!
#요약
#- 부울 자료형은 True와 False 두 가지 값만 가집니다.    
#- 비교 연산자(>, <, == 등)와 논리 연산자(and, or, not)를 사용하여 부울 값을 생성할 수 있습니다.
#- bool() 함수를 사용하여 다른 자료형을 부울 값으로 변환할 수 있습니다.
#- 부울 값은 조건문과 반복문에서 주로 사용됩니다.
#- 파이썬에서는 대문자 T와 F로 시작하는 True와 False를 사용합니다.  

#자료형의 참과 거짓
#참과 거짓 예제
true_values = [1, -1, 0.1, "Hello", [1, 2], (3, 4), {5: 'a'}]
false_values = [0, 0.0, "", [], (), {}, None]       
for value in true_values:
    print(f"{value}의 부울 값:", bool(value))  # 출력: 각 값의 부울 값: True
for value in false_values:
    print(f"{value}의 부울 값:", bool(value))  # 출력: 각 값의 부울 값: False
#출력 결과
# 1의 부울 값: True 
# -1의 부울 값: True
# 0.1의 부울 값: True
# Hello의 부울 값: True
# [1, 2]의 부울 값: True
# (3, 4)의 부울 값: True
# {5: 'a'}의 부울 값: True
# 0의 부울 값: False
# 0.0의 부울 값: False
# 의 부울 값: False
# []의 부울 값: False
# ()의 부울 값: False
# {}의 부울 값: False
#조건문에서 참과 거짓 활용 예제
values = [10, 0, "Python", "", [1, 2], []]
for value in values:
    if value:
        print(f"{value}는 참입니다.")  # 출력: 참인 값들
    else:
        print(f"{value}는 거짓입니다.")  # 출력: 거짓인 값들
#출력 결과
# 10는 참입니다.
# 0는 거짓입니다.
# Python는 참입니다.
# 는 거짓입니다.        
# [1, 2]는 참입니다.
# []는 거짓입니다.
#요약
#- 파이썬에서 참(True)과 거짓(False)은 부울 자료형
#- 숫자 0, 빈 문자열, 빈 리스트, 빈 튜플, 빈 딕셔너리, None 등은 거짓으로 간주됩니다.
#- 그 외의 값들은 모두 참으로 간주됩니다.   
#- 조건문과 반복문에서 참과 거짓을 활용하여 흐름 제어가 가능합니다.
#- bool() 함수를 사용하여 값의 부울 값을 확인할 수 있습니다.
#- 참과 거짓의 개념은 파이썬 프로그래밍에서 매우 중요합니다.
