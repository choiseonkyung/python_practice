# 6042
a = input()
b = round(float(a), 2)
print(b)

# 6043
a, b = input().split()
c = float(a)/float(b)
print(format(c, '.3f'))

# 6044
a, b = input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a) % int(b))
print(format(int(a)/int(b), '.2f'))

# 6045
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = a+b+c
avg = sum/3
print(sum, format(avg, '.2f'))

# 6046
n = input()
int_n = int(n)
print(int_n<<1)

# 6047
a, b = input().split()
int_a = int(a)
int_b = int(b)
print(int_a<<int_b)

# 6048
a, b = input().split()
int_a = int(a)
int_b = int(b)
if int_a < int_b:
    print(True)
else:
    print(False)

# 6049
a, b = input().split()
int_a = int(a)
int_b = int(b)
if int_a == int_b:
    print(True)
else:
    print(False)

# 6050
a, b = input().split()
int_a = int(a)
int_b = int(b)
if int_b >= int_a:
    print(True)
else:
    print(False)

# 6051
a, b = input().split()
int_a = int(a)
int_b = int(b)
if int_b != int_a:
    print(True)
else:
    print(False)

# 6052
n = input()
n = int(n)
print(bool(n))

# 6053
n = input()
n = bool(int(n))
print(not n)

# 6054
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(a and b)

# 6055
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(a or b)

# 6056
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(a and (not b) or (not a) and b)

# 6057
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and b) or (not a and not b))

# 6058
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(not a and not b)