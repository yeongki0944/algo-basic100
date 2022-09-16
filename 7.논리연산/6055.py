# 2개의 정수값이 입력될 때,
# 하나라도 참일 경우 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.


a, b = input().split()

a = int(a)
b = int(b)

r = bool(a) or bool(b)

print(r)
