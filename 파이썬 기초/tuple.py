#튜플 요솟값 삭제
a = (1, 2, 3, 4, 5)
# del a[2]  # TypeError: 'tuple' object doesn't support item deletion
print("튜플은 불변(immutable) 자료형이므로 요소를 삭제할 수 없습니다.")
# 출력 결과
# 튜플은 불변(immutable) 자료형이므로 요소를 삭제할 수 없습니다.

#튜플 메서드
# count(): 튜플에서 특정 값의 개수를 반환
fruits = ('apple', 'banana', 'apple', 'orange', 'banana', 'apple')
count_apple = fruits.count('apple')
print("apple의 개수:", count_apple)  # 출력: apple의 개수
# 출력 결과
# apple의 개수: 3
# index(): 튜플에서 특정 값의 첫 번째 인덱스를 반환
index_banana = fruits.index('banana')
print("banana의 첫 번째 인덱스:", index_banana)  # 출력: banana의 첫 번째 인덱스
# 출력 결과
# banana의 첫 번째 인덱스: 1
# 요약
# - 튜플은 불변(immutable) 자료형이므로 요소를 삭제하거나 변경할 수 없습니다.
# - count() 메서드는 튜플에서 특정 값의 개수를 반환합니다.
# - index() 메서드는 튜플에서 특정 값의 첫 번째 인덱스를 반환합니다.
# - 튜플은 리스트와 달리 요소를 추가, 삭제, 변경할 수 없습니다.
# - 튜플은 주로 변경되지 않는 데이터를 저장할 때 사용됩니다.
# - 튜플의 메서드는 요소의 개수 세기와 인덱스 찾기에 국한됩니다.
       

#튜플 슬라이싱 예시
data = (10, 20, 30, 40, 50, 60, 70)
subset = data[2:5]
print("부분 튜플 (2-5):", subset)  # 출력: 부분
# 출력 결과
# 부분 튜플 (2-5): (30, 40, 50)
subset2 = data[:3]
print("부분 튜플 (처음-3):", subset2)  # 출력: 부분 튜플 (처음-3): (10, 20, 30)
subset3 = data[4:]
print("부분 튜플 (4-끝):", subset3)  # 출력: 부분 튜플 (4-끝): (50, 60, 70)
# 출력 결과
# 부분 튜플 (처음-3): (10, 20, 30)  
# 부분 튜플 (4-끝): (50, 60, 70)
            

#튜플 더하기 곱하기
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# 튜플 더하기
combined_tuple = tuple1 + tuple2
print("튜플 더하기:", combined_tuple)  # 출력: 튜플 더하기: (1, 2, 3, 4, 5, 6)
# 튜플 곱하기
repeated_tuple = tuple1 * 3
print("튜플 곱하기:", repeated_tuple)  # 출력: 튜플 곱하기: (1, 2, 3, 1, 2, 3, 1, 2, 3)
# 출력 결과
# 튜플 더하기: (1, 2, 3, 4, 5, 6)
# 튜플 곱하기: (1, 2, 3, 1, 2, 3, 1, 2, 3)
      

#튜플 길이 구하기   
my_tuple = (10, 20, 30, 40, 50)
length = len(my_tuple)
print("튜플의 길이:", length)  # 출력: 튜플의 길이: 5
# 출력 결과
# 튜플의 길이: 5