'''
정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.

예시
n = int(input())
print(bool(n))

참고
bool( ) 을 이용하면 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력해준다.
식이나 값을 계산해서 결과값이 만들어지는 것을 평가(evaluate)라고 한다. 

python 언어에서 정수값 0은 False(거짓)로 평가되고, 그 외의 값들은 모두 True(참)로 평가된다.
** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.

정수 1개가 입력된다.
입력된 값이 0이면 False, 0이 아니면 True 를 출력한다.
'''

n = int(input())
print(bool(n))

'''
bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.  True, False -> instances 이고, Bool 클래스의 인스턴스임
The class bool is a subclass of the class int, and cannot be subclassed.  Bool은 int클래스의 하위클래스, / 하위클래스로 지정불가 ???? 뭔소리??
'''
