def foo(name, age):
    print(name, age)

foo("Ben", 25)

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

def calculation(a, b):
    return a+b, a-b

print(calculation(40, 10))


def showEmployee(name, salary=9000):
    print("Employee", name, "salary is:", salary)

showEmployee("Sem", 7000)
showEmployee("Sem")


def outerFun(a, b):
    square = a**2
    def innerFun(a,b):
        return a+b
    add = innerFun(a, b)
    return add+5

result = outerFun(5, 10)
print(result)

def calculate(n):
    if n:
        return n + calculate(n-1)
    else:
        return 0

r = calculate(10)
print(r)

def nmg(name, age):
    print(name, age)

nmg("Emma", 26)

man = nmg
man("Emma", 26)

print(list( range(4, 30, 2)))

aList = [4, 6, 8, 24, 12, 2]
print(max(aList))