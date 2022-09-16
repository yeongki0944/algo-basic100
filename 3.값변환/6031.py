# 10진 정수 1개를 입력받아 유니코드 문자로 출력해보자.


n = input()
n = int(n)

c = chr(n)
# Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

print(c)
