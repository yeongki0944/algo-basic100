# 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

a, b = input().split()
a = int(a)
b = int(b)

print(a)
print(b)


# 파이썬 콤파 사용법 - https://mingrammer.com/tips-of-using-comma-in-python/
# 다중값 할당, 반환


# 동시 선언 및 초기화
a, b = 1, 2

# 값 교환 (Swap)
a, b = b, a

# 다중값 반환


def add_and_mul(a, b):
    add = a + b
    mul = a * b
    return add, mul
