a, b, c = map(int, input().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)

# a,b,c=map(int,input().split())
# print(x:=(a+b)%c,x,y:=a*b%c,y)

# 바다코끼리 연산자
# https://int-i.github.io/python/2020-05-29/python-walrus-operator/
# 증명
# https://st-lab.tistory.com/214
