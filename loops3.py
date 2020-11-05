print("3.1\n")
i = 0
while i <= 10:
    print(i)
    i += 1
print("\n")
print("3.2\n")
a = 6
for i in range(1, a):
    for column in range(1, i + 1):
        print(column, end=' ')
    print(" ")

print("\n")
print("3.3\n")
sum = 0
n = int(input("Please enter number "))
for i in range(1, n+1, 1):
    sum += i
print("\n")
print("Sum is: ", sum)

print("\n")
print("3.4\n")
a = 2
for i in range(1, 11, 1):
    s = a*i
    print(s)

print("\n")
print("3.5\n")
l = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in l:
    if (i > 150):
        break
    if(i % 5 == 0):
        print(i)

print("\n")
print("3.6\n")
n= 75869
c = 0
while n != 0:
    n //= 10
    c+= 1
print(c)

print("\n")
print("3.7\n")
a = 6
for i in range(0, a):
    for k in range(a-i,0,-1):
        print(k, end=' ')
    print(" ")

print("\n")
print("3.8\n")
l=[10,20,30,40,50]
a=len(l)+1
b=0-a
i=-1

while i>b:

    print(l[i])
    i=i-1

print("\n")
print("3.9\n")
for n in range(-10, 0, 1):
    print(n)
print("\n")
print("3.10\n")
for i in range(5):
    print(i)
else:
    print("Done")
print("\n")
print("3.11\n")
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for n in range(25, 50 + 1):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n)

print("\n")
print("3.12\n")
terms = 10
# first two terms
num1, num2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < terms:
    print(num1, end="  ")
    temp = num1 + num2
    num1 = num2
    num2 = temp
    count += 1
print("\n")
print("3.13\n")
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

print("\n")
print("3.14\n")
n = 76542
m = 0
print("Given Number ", n)
while n > 0:
    r = n % 10
    m = (m * 10) + r
    n = n // 10
print(m)
print("\n")
print("3.15\n")
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in list[1::2]:
    print(i, end=" ")
print("\n\n3.16\n")
n = 6
for i in range(1, n + 1):
    print(" Number is :", i, " i cube is", (i * i * i))

print("\n\n3.17\n")
n = 5
a = 2
s = 0
for i in range(0, n):
    print(a, end=" ")
    s += a
    start = (a * 10) + 2
print("\nSum of above series is:", s)

print("\n\n3.18\n")

k = 5
for i in range(0, k):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(k, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

