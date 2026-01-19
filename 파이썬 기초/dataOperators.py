#데이터 연산방법

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b    
def modulus(a, b):
    return a % b
def exponent(a, b):
    return a ** b
def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a // b
print("덧셈:", add(10, 5))            # 출력: 덧셈: 15
print("뺄셈:", subtract(10, 5))       # 출력: 뺄셈: 5
print("곱셈:", multiply(10, 5))       # 출력: 곱셈: 50
print("나눗셈:", divide(10, 5))       # 출력: 나눗셈: 2.0
print("나머지:", modulus(10, 3))      # 출력: 나머지: 1
print("거듭제곱:", exponent(2, 3))    # 출력: 거듭제곱: 8
print("몫:", floor_divide(10, 3))     # 출력: 몫: 3
# 출력 결과
# 덧셈: 15
# 뺄셈: 5
# 곱셈: 50
# 나눗셈: 2.0
# 나머지: 1
# 거듭제곱: 8
# 몫: 3
# 요약
# - 기본적인 산술 연산을 함수로 구현하여 재사용 가능하게 함
# - 나눗셈과 몫 연산에서 0으로 나누는 경우를 처리하여 오류 방지 
print("집합:", unique_numbers)  # 출력: 집합: {1, 2, 3}
# 사전 활용 예시
person = {'name': 'Alice', 'age': 30}
person['age'] = 31  # 값 수정
person['city'] = 'New York'  # 새로운 키-값 쌍 추가

print("사전:", person)  # 출력: 사전: {'name': 'Alice', 'age': 31, 'city': 'New York'}
# 출력 결과
