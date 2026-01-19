# 데이터 자료형

# 파이썬의 주요 데이터 자료형에는 다음과 같은 것들이 있습니다.
# 1. 숫자형 (Numeric Types)
#    - int: 정수형 (예: 1, -5, 42)
#    - float: 부동소수점형 (예: 3.14, -0.001, 2.0)
#    - complex: 복소수형 (예: 1+2j, 3-4j)
# 2. 문자열형 (String Type)
#    - str: 문자열형 (예: "Hello", 'Python', """Multiline String""")
# 3. 불린형 (Boolean Type)
#    - bool: 불린형 (예: True, False)
# 4. 리스트형 (List Type)
#    - list: 리스트형 (예: [1, 2, 3], ['a', 'b', 'c'], [1, 'a', 3.5])
# 5. 튜플형 (Tuple Type)
#    - tuple: 튜플형 (예: (1, 2), ('x', 'y', 'z'), (1, 'a', 3.5))
# 6. 집합형 (Set Type)
#    - set: 집합형 (예: {1, 2, 3}, {'a', 'b', 'c'})
# 7. 사전형 (Dictionary Type)
#    - dict: 사전형 (예: {'key1': 'value1', 'key2': 'value2'})
# 8. None형 (None Type)
#    - NoneType: None형 (예: None)
# 각 자료형은 특정한 용도와 특성을 가지고 있으며, 파이썬에서 데이터를 다룰 때 중요한 역할을 합니다.

# 예시 코드

# 숫자형
a = 10          # int
b = 3.14        # float
c = 1 + 2j     # complex
print(type(a), type(b), type(c))
# 문자열형
s = "Hello, World!"  # str
print(type(s))
# 불린형
flag = True         # bool
print(type(flag))
# 리스트형
my_list = [1, 2, 3, 'a', 'b']  # list
print(type(my_list))
# 튜플형
my_tuple = (1, 2, 3, 'x', 'y')  # tuple
print(type(my_tuple))
# 집합형
my_set = {1, 2, 3, 'a', 'b'}    # set
print(type(my_set))
# 사전형
my_dict = {'name': 'Alice', 'age': 30}  # dict
print(type(my_dict))
# None형
nothing = None          # NoneType
print(type(nothing))


# 출력 결과
# <class 'int'> <class 'float'> <class 'complex'>
# <class 'str'>
# <class 'bool'>
# <class 'list'>
# <class 'tuple'>
# <class 'set'>
# <class 'dict'>
# <class 'NoneType'>

#8진수와 16진수 표현
octal_num = 0o12  # 8진수 12는 10진수로 10
hex_num = 0xA    # 16진수 A는 10진수로 10
print(octal_num, hex_num)  # 출력: 10 10
# 출력 결과
# 10 10

# 진법 변환 함수
decimal_num = 10
print(bin(decimal_num))   # 2진수 출력: 0b1010
print(oct(decimal_num))   # 8진수 출력: 0o12
print(hex(decimal_num))   # 16진수 출력: 0xa
# 출력 결과
# 0b1010
# 0o12
# 0xa

# 형 변환 함수
num_str = "123"
num_int = int(num_str)      # 문자열을 정수로 변환
num_float = float(num_str)  # 문자열을 실수로 변환
print(num_int, num_float)   # 출력: 123 123.0
# 출력 결과
# 123 123.0
# 문자열 변환
num = 456
num_to_str = str(num)      # 정수를 문자열로 변환
print(num_to_str)          # 출력: "456"    
# 출력 결과
# 456

# 불린 변환
zero = 0
non_zero = 42
print(bool(zero))      # 출력: False
print(bool(non_zero))  # 출력: True
# 출력 결과
# False
# true

# 리스트 변환
andy = (1, 2, 3)
andy_list = list(andy)  # 튜플을 리스트로 변환  
print(andy_list)        # 출력: [1, 2, 3]
# 출력 결과
# [1, 2, 3]

# 튜플 변환
bruce = [4, 5, 6]
bruce_tuple = tuple(bruce)  # 리스트를 튜플로 변환
print(bruce_tuple)         # 출력: (4, 5, 6)
# 출력 결과
# (4, 5, 6)
# 집합 변환
clark = [7, 8, 9, 7]
clark_set = set(clark)  # 리스트를 집합으로 변환 (중복 제거)
print(clark_set)       # 출력: {8, 9, 7}
# 출력 결과
# {8, 9, 7}
# 사전 변환
diana = [('name', 'Diana'), ('age', 28)]
diana_dict = dict(diana)  # 리스트를 사전으로 변환
print(diana_dict)        # 출력: {'name': 'Diana', 'age': 28}
# 출력 결과
# {'name': 'Diana', 'age': 28}
# 요약
# 파이썬에서는 다양한 데이터 자료형을 제공하며, 각 자료형은 특정한 용도와 특성을 가지고 있습니다. 또한, 형 변환 함수를 통해 서로 다른 자료형 간의 변환이 가능합니다.

# 리스트, 튜플, 집합, 사전의 차이점 정리
# 리스트 (list)
# - 순서가 있음 (ordered)  
# - 변경 가능 (mutable)
# - 중복된 값 허용
# 튜플 (tuple)
# - 순서가 있음 (ordered)
# - 변경 불가능 (immutable)
# - 중복된 값 허용
# 집합 (set)
# - 순서가 없음 (unordered)
# - 변경 가능 (mutable)
# - 중복된 값 허용하지 않음
# 사전 (dict)
# - 키-값 쌍으로 구성 (key-value pairs)
# - 순서가 없음 (unordered) (Python 3.7 이상에서는 삽입 순서 유지)
# - 변경 가능 (mutable)
# - 키는 중복될 수 없음 (값은 중복 가능)
# 이러한 차이점을 이해하면 데이터 구조를 선택하고 활용하는 데 도움이 됩니다.
# 예시 코드로 차이점 설명

# 리스트 예시
my_list = [1, 2, 2, 3]
print("리스트:", my_list)  # 출력: 리스트: [1, 2, 2, 3]
# 튜플 예시
my_tuple = (1, 2, 2, 3)
print("튜플:", my_tuple)  # 출력: 튜플: (1, 2, 2, 3)
# 집합 예시
my_set = {1, 2, 2, 3}
print("집합:", my_set)    # 출력: 집합: {1, 2, 3}
# 사전 예시
my_dict = {'a': 1, 'b': 2, 'a': 3}
print("사전:", my_dict)   # 출력: 사전: {'a': 3, 'b': 2}
# 출력 결과
# 리스트: [1, 2, 2, 3]
# 튜플: (1, 2, 2, 3)
# 집합: {1, 2, 3}
# 사전: {'a': 3, 'b': 2}
# 요약
# - 리스트와 튜플은 순서가 있으며 중복된 값을 허용합니다.
# - 집합은 순서가 없고 중복된 값을 허용하지 않습니다. 
# - 사전은 키-값 쌍으로 구성되며, 키는 중복될 수 없습니다.

#리스트와 튜플의 활용 예시
# 리스트 활용 예시
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')  # 리스트에 요소 추가
print("리스트:", fruits)  # 출력: 리스트: ['apple', 'banana', 'cherry', 'date']
# 튜플 활용 예시
coordinates = (10.0, 20.0)
# coordinates[0] = 15.0  # 오류 발생: 튜플은 변경 불가능
print("튜플:", coordinates)  # 출력: 튜플: (10.0, 20.0)
# 출력 결과
# 리스트: ['apple', 'banana', 'cherry', 'date']
# 튜플: (10.0, 20.0)
# 요약
# - 리스트는 변경이 가능하여 데이터를 추가, 삭제, 수정할 수 있습니다.
# - 튜플은 변경이 불가능하여 고정된 데이터를 저장할 때 유용합니다.

#집합과 사전의 활용 예시
# 집합 활용 예시
unique_numbers = {1, 2, 3}
unique_numbers.add(2)  # 중복된 값 추가 시도 (무시됨)
unique_numbers.add(4)  # 새로운 값 추가
print("집합:", unique_numbers)  # 출력: 집합: {1, 2, 3, 4}
# 사전 활용 예시
person = {'name': 'Alice', 'age': 30}
person['age'] = 31  # 값 수정
person['city'] = 'New York'  # 새로운 키-값 쌍 추가
print("사전:", person)  # 출력: 사전: {'name': 'Alice', 'age': 31, 'city': 'New York'}
# 출력 결과
# 집합: {1, 2, 3, 4}
# 사전: {'name': 'Alice', 'age': 31, 'city': 'New York'}
# 요약
# - 집합은 중복된 값을 허용하지 않으며, 새로운 값을 추가할 수 있습니다.
# - 사전은 키-값 쌍으로 데이터를 저장하며, 값을 수정하거나 새로운 키-값 쌍을 추가할 수 있습니다.