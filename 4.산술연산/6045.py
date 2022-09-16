# 정수 3개를 입력받아 합과 평균을 출력해보자.
# 평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.

a, b, c = input().split()

# split() - Return a list of the words in the string, using sep as the delimiter string.

a = int(a)
b = int(b)
c = int(c)

r1 = a+b+c
r2 = r1 / 3

print(r1, format(r2, ".2f"))
