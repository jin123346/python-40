#딕셔너리 쌍 추가, 삭제, 수정 및 조회 예제
#딕셔너리 생성
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
#딕셔너리 쌍 추가   
my_dict['job'] = 'Engineer'
print("추가 후 딕셔너리:", my_dict)  # 출력: 추가 후 딕셔너리: {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}
#딕셔너리 쌍 수정
my_dict['age'] = 26
print("수정 후 딕셔너리:", my_dict)  # 출력: 수정 후 딕셔너리: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}
#딕셔너리 쌍 삭제
del my_dict['city']
print("삭제 후 딕셔너리:", my_dict)  # 출력: 삭제 후 딕셔너리: {'name': 'Alice', 'age': 26, 'job': 'Engineer'}
#딕셔너리 쌍 조회
name = my_dict['name']  
print("이름 조회:", name)  # 출력: 이름 조회: Alice
#출력 결과
# 추가 후 딕셔너리: {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}
# 수정 후 딕셔너리: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}
# 삭제 후 딕셔너리: {'name': 'Alice', 'age': 26, 'job': 'Engineer'}
# 이름 조회: Alice  
#요약
#- 딕셔너리는 키-값 쌍으로 데이터를 저장하는 자료형입니다.
#- 딕셔너리 쌍은 대괄호([])를 사용하여 추가, 수정, 삭제 및 조회할 수 있습니다.
#- 추가: my_dict['new_key'] = value
#- 수정: my_dict['existing_key'] = new_value
#- 삭제: del my_dict['key_to_delete']
#- 조회: value = my_dict['key_to_lookup']
#- 딕셔너리는 순서가 없으며, 키는 고유해야 합니다.
#- 딕셔너리는 다양한 데이터 타입의 값을 저장할 수 있습니다.


#KEY 값으로 VALUE 값 가져오기
person = {'name': 'Bob', 'age': 30, 'city': 'San Francisco'}
age = person['age']
print("나이:", age)  # 출력: 나이: 30   
#출력 결과
# 나이: 30
#딕셔너리에서 키가 존재하지 않을 때의 처리
person = {'name': 'Bob', 'age': 30}
city = person.get('city', 'Unknown')
print("도시:", city)  # 출력: 도시: Unknown
#출력 결과
# 도시: Unknown
#딕셔너리 키-값 쌍 모두 가져오기
person = {'name': 'Bob', 'age': 30, 'city': 'San Francisco'}
keys = person.keys()
values = person.values()
items = person.items()
print("키들:", list(keys))        # 출력: 키들: ['name', 'age', 'city']
print("값들:", list(values))     # 출력: 값들: ['Bob', 30, 'San Francisco']
print("키-값 쌍들:", list(items))  # 출력: 키-값 쌍들: [('name', 'Bob'), ('age', 30), ('city', 'San Francisco')]
#출력 결과
# 키들: ['name', 'age', 'city']
# 값들: ['Bob', 30, 'San Francisco']
# 키-값 쌍들: [('name', 'Bob'), ('age', 30), ('city', 'San Francisco')]
#딕셔너리 쌍 반복문 예제
person = {'name': 'Bob', 'age': 30, 'city': 'San Francisco'}
for key, value in person.items():
    print(f"{key}: {value}")
#출력 결과
# name: Bob
# age: 30   
# city: San Francisco




#key로 value 값 가져오기 예제
data = {'fruit': 'apple', 'color': 'red', 'quantity': 5}
fruit = data['fruit']
print("과일:", fruit)  # 출력: 과일: apple
#출력 결과
# 과일: apple
#딕셔너리에서 키가 존재하지 않을 때 기본값 반환 예제
data = {'fruit': 'apple', 'color': 'red'}
quantity = data.get('quantity', 0)
print("수량:", quantity)  # 출력: 수량: 0
#출력 결과
# 수량: 0
#딕셔너리의 키, 값, 키-값 쌍 가져오기 예제
data = {'fruit': 'apple', 'color': 'red', 'quantity': 5}
keys = data.keys()      
values = data.values()
items = data.items()
print("키들:", list(keys))        # 출력: 키들: ['fruit', 'color', 'quantity']
print("값들:", list(values))     # 출력: 값들: ['apple', 'red', 5]
print("키-값 쌍들:", list(items))  # 출력: 키-값 쌍들: [('fruit', 'apple'), ('color', 'red'), ('quantity', 5)]
#출력 결과
# 키들: ['fruit', 'color', 'quantity']
# 값들: ['apple', 'red', 5]
# 키-값 쌍들: [('fruit', 'apple'), ('color', 'red'), ('quantity', 5)]


#딕셔너리 get() 메서드와 remove() 메서드 사용 예제
data = {'fruit': 'apple', 'color': 'red', 'quantity': 5}
# get() 메서드 사용
fruit = data.get('fruit', 'Unknown')
print("과일:", fruit)  # 출력: 과일: apple
# remove() 메서드 사용 (딕셔너리에서 키-값 쌍을 제거)
removed_value = data.pop('color', None)
print("제거된 값:", removed_value)  # 출력: 제거된 값: red
print("제거 후 딕셔너리:", data)  # 출력: 제거 후 딕셔너리: {'fruit': 'apple', 'quantity': 5}
#출력 결과
# 과일: apple
# 제거된 값: red
# 제거 후 딕셔너리: {'fruit': 'apple', 'quantity': 5}   

#조사하기 in 연산자 사용 예제
data = {'fruit': 'apple', 'color': 'red', 'quantity': 5}
# 키 존재 여부 확인
has_color = 'color' in data
print("color 키 존재 여부:", has_color)  # 출력: color 키 존재 여부: True
# 값 존재 여부 확인
has_banana = 'banana' in data.values()
print("banana 값 존재 여부:", has_banana)  # 출력: banana 값 존재 여부
# 출력: banana 값 존재 여부: False
#출력 결과
# color 키 존재 여부: True
# banana 값 존재 여부: False


#요약
#- 딕셔너리에서 키로 값을 가져올 때는 대괄호    ([]) 또는 get() 메서드를 사용합니다.
#- get() 메서드는 키가 없을 때 기본값을 반환할 수 있어 유용합니다.
#- keys(), values(), items() 메서드를 사용하여 딕셔너리의 키, 값, 키-값 쌍을 각각 가져올 수 있습니다.
#- for 루프를 사용하여 딕셔너리의 키-값 쌍을 반복할 수 있습니다.
#- 딕셔너리는 매우 유연한 자료형으로 다양한 용도로 사용됩니다.


