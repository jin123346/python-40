#홍길동씨의 과목별 점수 평균 구하기 
scores = {
    '국어': 80,
    '영어': 75,
    '수학': 55}

total= sum(scores.values())
size = len(scores)
average = total / size
print("총점:", total)          # 출력: 총점: 210
print("평균점수:", average)     # 출력: 평균점수: 70.0



#자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법
number = 13
if number % 2 == 0:
    print(f"{number}는 짝수입니다.")  # 출력: 13는 짝수입니다.
else:
    print(f"{number}는 홀수입니다.")  # 출력: 13는 홀수입니다.
#출력 결과
# 13는 홀수입니다.

#홍길동씨의 주민등록번호 881120-1068234이다. 홍길동씨의 주민등록 번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
jumin = "881120-1068234"
data_of_birth= "19"+jumin[:6]
number = jumin[7:]
print("연월일:", data_of_birth)  # 출력: 연월일: 881120
print("뒤의 숫자:", number)       # 출력: 뒤의 숫자: 1068234
#출력 결과
# 연월일: 881120
# 뒤의 숫자: 1068234



#주민번호에서 성별 여부 확인

sex= number[0]

if sex in ['1','3']:
    print("남자입니다.")  # 출력: 남자입니다.   
else:
    print("여자입니다.")  # 출력: 여자입니다.
#출력 결과
# 남자입니다.


#문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해보자
a="a:b:c:d"
a_replaced= a.replace(':', '#')
print(a_replaced)  # 출력: a#b#c#d
#출력 결과
# a#b#c#d


#[1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어 보자.
numbers = [1,3,5,4,2]   
a=numbers[:]

numbers.sort(reverse=True)
print(numbers)  
# 출력: [5, 4, 3, 2, 1]
a.sort()
a.reverse()
print(a)
#출력 결과  
# [5, 4, 3, 2, 1]


#['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
words = ['Life', 'is', 'too', 'short']
sentence = ' '.join(words)
print(sentence)  # 출력: Life is too short
#출력 결과
# Life is too short

#(1,2,3) 튜플에 4라는 숫자를 추가하여 (1,2,3,4)로 만들어 출력해 보자.
tuple=(1,2,3)
tuple= tuple.__add__((4,))
tuple= tuple + (5,)
print(tuple)  # 출력: (1, 2, 3, 4)


#딕셔너리 a가 있다
a=dict()
print(a)  # 출력: {}

#다음중 오류 발생하는 경우 고르기
a['name'] = 'python'
a[('a',)] = 'python'
#a[[1]] = 'python'  # 오류 발생 # 리스트는 변경 가능해서 키로 사용할 수 없음
a[250] = 'python'
print(a)
#출력 결과
# {'name': 'python', ('a',): 'python', 250: 'python'}

#딕서녀리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {'A':90, 'B':80, 'C':70}
result = a['B']
print(a)  # 출력: {'A':90, 'B':80, 'C':70}
print(result)
#출력 결과
# 80


#a 리스트에서 중복 숫자를 제거해보자
a=[1,1,1,2,2,3,3,3,4,4,5]
a=set(a)
b=list(a)

print(b)  # 출력: [1, 2, 3, 4, 5]
#출력 결과
# [1, 2, 3, 4, 5]

#다음 코드의 실행 결과를 예상해보자.
a = b = [1, 2, 3]
a[1]=4
print(b)  # 출력: [1, 4, 3]
#출력 결과
# [1, 4, 3]