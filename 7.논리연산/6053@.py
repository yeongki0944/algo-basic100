# 정수 1개가 입력된다.
# 입력된 정수의 불 값이 False 이면 True, True 이면 False 를 출력한다.
# 참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서 not 예약어(reserved word, keyword)를 사용할 수 있다.


n = int(input())

r = not bool(n)

print(r)
