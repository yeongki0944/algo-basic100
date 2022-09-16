# 2개의 정수값이 입력될 때,
# 두 값의 True / False 값이 서로 다를 경우만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.
# xor 에 대해서 and or not으로 구현필요
# api는 없나?


a, b = input().split()

a = int(a)
b = int(b)

r = (a and (not bool(b))) or ((not a) and bool(b))

print(r)
