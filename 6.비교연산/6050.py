'''
두 정수(a, b)가 공백을 두고 입력된다.
b가 a보다 크거나 같은 경우 True 를, 그렇지 않은 경우 False 를 출력한다.
'''

a, b = input().split()

a = int(a)
b = int(b)

print(a <= b)
