#if문
age = 20
if age >= 18:
    print("성인입니다.")
    print("환영합니다.")
# 출력: 성인입니다.
# 환영합니다.   
# if문 조건이 참이므로 들여쓰기 된 두 문장이 모두 실행된다.
else:
    print("미성년자입니다.")
    print("죄송합니다.")
# 출력: 미성년자입니다.
# 죄송합니다.   
# if문 조건이 참이므로 else 아래 들여쓰기 된 두 문장이 실행되지 않는다. 

#들여쓰기 주의
#if 문을 만들때는 if 조건문 : 바로 아래 문장부터 if문에 속하는 문장임을 표시하기 위해 들여쓰기를 해야 한다.
# 들여쓰기를 하지 않으면 if문에 속하는 문장이 아니게 되어 의도한 대로 동작하지 않을 수 있다.

money= True
if money:
    print("택시를") 
    print("타고")
#       print("가라")  => 들여쓰기 오류발생
else:
    print("걸어가라") 

#비교 연산자
x = 10
print(x > 5)    # 출력: True    
print(x < 5)    # 출력: False
print(x >= 10)  # 출력: True
print(x <= 10)  # 출력: True
print(x == 10)  # 출력: True
print(x != 10)  # 출력: False
#논리 연산자
a = True
b = False
print(a and b)  # 출력: False
print(a or b)   # 출력: True
print(not a)    # 출력: False
print(not b)    # 출력: True
#and: 둘다 참일때만 참 / or: 둘중 하나만 참이어도 참 / not: 참은 거짓으로 거짓은 참으로
# x in s , x not in s
# x가 s라는 집합에 포함되어 있는지 여부를 판단
print(3 in [1,2,3])        # 출력: True
print(4 in [1,2,3])        # 출력: False    
print('a' in 'apple')      # 출력: True
print('b' in 'apple')      # 출력: False    
print(3 not in [1,2,3])    # 출력: False
print(4 not in [1,2,3])    # 출력: True
print('a' not in 'apple')  # 출력: False
print('b' not in 'apple')  # 출력: True
#연습문제
# a만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라.
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")  # 출력: 택시를 타고 가라
else:
    print("걸어가라")  # 출력: 걸어가라
#출력 결과
# 택시를 타고 가라

#elif
#주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라.
pocket2=['paper','cellphone']
card = True

if 'money' in pocket2:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")
    
    

#조건부 표현식

score=80

if score >= 60:
    message="success"
else:
    message="failure"