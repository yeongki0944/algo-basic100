# 2개의 정수값이 입력될 때,
# 두 값의 True / False 값이 모두 False 일 때만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.


a, b = input().split()

a = bool(int(a))
b = bool(int(b))

r = (not a and not b)

print(r)
