# 6063
a, b = input().split()
a = int(a)
b = int(b)
c = (a if a >= b else b)
print(c)

# 6064
# 잘 안됨 ㅜ

# 6065
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 6066
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a % 2 == 0:
    print("even")
else:
    print("odd")

if b % 2 == 0:
    print("even")
else:
    print("odd")

if c % 2 == 0:
    print("even")
else:
    print("odd")

# 6067
n = int(input())
if n < 0:
    if n % 2 ==0:
        print('A')
    else:
        print('B')
else:
    if n % 2 ==0:
        print('C')
    else:
        print('D')

# 6068
n = int(input())
if n >= 90:
    print('A')
elif n >= 70:
    print('B')
elif n >= 40:
    print('C')
else:
    print('D')

# 6069
eval = input()
if eval == 'A':
    print('best!!!')
elif eval == 'B':
    print('good!!')
elif eval == 'C':
    print('run!')
elif eval =='D':
    print('slowly~')
else:
    print('what?')

# 6070
n = int(input())
if n // 3 == 1:
    print('spring')
elif n // 3 == 2:
    print('summer')
elif n // 3 == 3:
    print('fall')
else:
    print('winter')

# 6071
n = 1
while n != 0:
    n = int(input())
    if n!=0:
        print(n)
    if n==0:
        break