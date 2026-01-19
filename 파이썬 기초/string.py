#문자열 인덱싱과 슬라이싱
text = "Hello, World!"
print("원본 문자열:", text)  # 출력: 원본 문자열: Hello, World!
# 인덱싱
first_char = text[0]
last_char = text[-1]
print("첫 번째 문자:", first_char)  # 출력: 첫 번째 문자: H
print("마지막 문자:", last_char)   # 출력: 마지막 문자: !
# 슬라이싱
substring = text[7:12]
print("부분 문자열 (7-12):", substring)  # 출력: 부분 문자열 (7-12): World
# 출력 결과
# 원본 문자열: Hello, World!
# 첫 번째 문자: H
# 마지막 문자: !
# 부분 문자열 (7-12): World
# 요약

# - 문자열은 인덱싱을 통해 개별 문자에 접근할 수 있습니다.
# - 슬라이싱을 통해 문자열의 일부분을 추출할 수 있습니다.
# 문자열 연결과 반복
str1 = "Hello"
str2 = "World"
# 문자열 연결
concatenated = str1 + ", " + str2 + "!"
print("문자열 연결:", concatenated)  # 출력: 문자열 연결: Hello, World!
# 문자열 반복
repeated = str1 * 3
print("문자열 반복:", repeated)  # 출력: 문자열 반복: HelloHelloHello
# 출력 결과
# 문자열 연결: Hello, World!

# 문자열 반복: HelloHelloHello
# 요약
# - 문자열은 '+' 연산자를 사용하여 연결할 수 있습니다.
# - '*' 연산자를 사용하여 문자열을 반복할 수 있습니다.  
# 문자열 메서드 활용
sample_text = "  Python Programming Language  "
# 대문자 변환
upper_text = sample_text.upper()
print("대문자 변환:", upper_text)  # 출력: 대문자 변환:   PYTHON PROGRAMMING LANGUAGE
# 소문자 변환
lower_text = sample_text.lower()
print("소문자 변환:", lower_text)  # 출력: 소문자 변환:   python programming language
# 공백 제거
trimmed_text = sample_text.strip()
print("공백 제거:", trimmed_text)  # 출력: 공백 제거: Python Programming Language
# 문자열 치환\
replaced_text = sample_text.replace("Python", "Java")
print("문자열 치환:", replaced_text)  # 출력: 문자열 치환:   Java Programming Language
# 출력 결과
# 대문자 변환:   PYTHON PROGRAMMING LANGUAGE
# 소문자 변환:   python programming language
# 공백 제거: Python Programming Language
# 문자열 치환:   Java Programming Language
# 요약
# - 문자열 메서드를 사용하여 다양한 문자열 조작이 가능합니다.
# - 대문자/소문자 변환, 공백 제거, 문자열 치환 등이 자주 사용됩니다.
# 문자열 포매팅 예시
name = "Alice"
age = 30
# f-string 포매팅
formatted_str = f"My name is {name} and I am {age} years old."
print("f-string 포매팅:", formatted_str)  # 출력: f-string 포매팅: My name is Alice and I am 30 years old.
# format() 메서드 포매팅
formatted_str2 = "My name is {} and I am {} years old.".format(name, age)
print("format() 메서드 포매팅:", formatted_str2)  # 출력: format() 메서드 포매팅: My name is Alice and I am 30 years old.
# 출력 결과
# f-string 포매팅: My name is Alice and I am 30 years old.
# format() 메서드 포매팅: My name is Alice and I am 30 years old.
# 요약
# - f-string과 format() 메서드를 사용하여 문자열에 변수를 쉽게 삽입할 수 있습니다.
# - f-string은 Python 3.6 이상에서 사용 가능하며, 가독성이 좋습니다.
# 숫자형과 문자열의 변환 예시
num = 100
# 숫자형을 문자열로 변환
num_to_str = str(num)
print("숫자형을 문자열로 변환:", num_to_str)  # 출력: 숫자형을 문자열로 변환: 100
# 문자열을 숫자형으로 변환
str_num = "250" 
str_to_num = int(str_num)
print("문자열을 숫자형으로 변환:", str_to_num)  # 출력: 문자열을 숫자형으로 변환: 250
# 출력 결과
# 숫자형을 문자열로 변환: 100
# 문자열을 숫자형으로 변환: 250
# 요약
# - str() 함수를 사용하여 숫자형을 문자열로 변환할 수 있습니다.
# - int() 또는 float() 함수를 사용하여 문자열을 숫자형으로 변환할 수 있습니다.
# - 올바른 형식의 문자열만 숫자형으로 변환할 수 있습니다.
# - f-string과 format() 메서드를 사용하여 문자열에 변수를 쉽게 삽입할 수 있습니다.
# - f-string은 Python 3.6 이상에서 사용 가능하며, 가독성이 좋습니다.



# 문자열 슬라이싱 예시  
text = "Hello, World!"
substring = text[7:12]
print("부분 문자열 (7-12):", substring)  # 출력: 부분 문자열 (7-12): World

substring2 = text[:5]
print("부분 문자열 (처음-5):", substring2)  # 출력: 부분 문자열 (처음-5): Hello
substring3 = text[7:]
print("부분 문자열 (7-끝):", substring3)  # 출력: 부분 문자열 (7-끝): World!    

# 출력 결과
# 부분 문자열 (7-12): World
# 부분 문자열 (처음-5): Hello
# 부분 문자열 (7-끝): World!

# 문자열 포맷코드 종류
# %s: 문자열 (string)
# %d: 정수 (integer)
# %f: 부동 소수점 숫자 (floating-point number)
# %.2f: 소수점 이하 2자리까지 표시 (floating-point number with 2 decimal places)
# %o: 8진수 (octal)
# %x: 16진수 (hexadecimal)
# %% : 퍼센트 기호 (%) 출력




