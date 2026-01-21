#리스트 관련 함수 
# append(): 리스트의 마지막에 새로운 요소를 추가
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  # 출력: ['apple', 'banana', 'cherry', 'orange']
# 출력 결과
# ['apple', 'banana', 'cherry', 'orange']

# extend(): 리스트에 여러 요소를 한 번에 추가
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # 출력: [1, 2, 3, 4, 5, 6]
# 출력 결과
# [1, 2, 3, 4, 5, 6]

# insert(): 특정 위치에 요소를 삽입
colors = ['red', 'blue', 'green']
colors.insert(1, 'yellow')
print(colors)  # 출력: ['red', 'yellow', 'blue', 'green']
# 출력 결과
# ['red', 'yellow', 'blue', 'green']

# remove(): 특정 값을 가진 첫 번째 요소를 제거
animals = ['cat', 'dog', 'bird', 'dog']
animals.remove('dog')
print(animals)  # 출력: ['cat', 'bird', 'dog']
# 출력 결과
# ['cat', 'bird', 'dog']
# pop(): 특정 위치의 요소를 제거하고 반환 (기본값은 마지막 요소)
cities = ['New York', 'Los Angeles', 'Chicago']
removed_city = cities.pop(1)
print(removed_city)  # 출력: Los Angeles
print(cities)       # 출력: ['New York', 'Chicago']
# 출력 결과
# Los Angeles
# ['New York', 'Chicago']
# index(): 특정 값의 첫 번째 인덱스를 반환
numbers = [10, 20, 30, 20, 40]
index_of_20 = numbers.index(20)
print(index_of_20)  # 출력: 1
# 출력 결과
# 1
# count(): 특정 값의 개수를 반환
letters = ['a', 'b', 'a', 'c', 'a']
count_of_a = letters.count('a')
print(count_of_a)  # 출력: 3
# 출력 결과
# 3
# sort(): 리스트를 오름차순으로 정렬
values = [5, 2, 9, 1, 5, 6]
values.sort()
print(values)  # 출력: [1, 2, 5, 5, 6, 9]
# 출력 결과
# [1, 2, 5, 5, 6, 9]
# reverse(): 리스트의 요소 순서를 반대로 뒤집기
chars = ['a', 'b', 'c', 'd']
chars.reverse()
print(chars)  # 출력: ['d', 'c', 'b', 'a']
# 출력 결과
# ['d', 'c', 'b', 'a']
# 요약
# - 리스트는 다양한 메서드를 제공하여 요소를 추가, 제거, 검색 및 정렬할 수 있습니다.
# - append(), extend(), insert() 등을 사용하여 요소를 추가할 수 있습니다.
# - remove(), pop() 등을 사용하여 요소를 제거할 수 있습니다.
# - index(), count() 등을 사용하여 요소를 검색할 수 있습니다.
