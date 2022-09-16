# 2개의 정수값이 입력될 때,
# 둘 다 True 일 경우에만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

a, b = input().split()

a = int(a)
b = int(b)

r = bool(a) and bool(b)

print(r)
