
'''
3개의 요소로 이루어지는 3항 연산은
"x if C else y" 의 형태로 작성이 된다.
- C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
- x : C의 평가 결과가 True 일 때 사용할 값
- y : C의 평가 결과가 True 가 아닐 때 사용할 값

조건식 또는 값이 True 이면 x 값이 사용되고, True가 아니면 y 값이 사용되도록 하는 코드이다.

예를 들어
0 if 123>456 else 1
과 같은 표현식의 평가값은 123 > 456 의 비교연산 결과가 False 이므로 1이 된다.

예시 코드에서
a>=b 의 결과가 True(참) 이면 (a if (a>=b) else b)의 결과는 a가 되고,
a>=b 의 결과가 False(거짓)이면 (a if (a>=b) else b)의 결과는 b가 된다.

(a if a>b else b) if ((a if a>b else b)>c) else c
'''

# 3개의 정수가 공백으로 구분되어 입력된다.
# 가장 작은 값을 출력한다.

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

n1 = a if (a < b) else b


print(n1 if (n1 < c) else c)
