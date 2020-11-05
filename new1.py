print("1.1\n")
def sum(a,b):
    p=a*b
    if(p<1000):
        return p
    else:
        return a+b

a=50
b=100
r=sum(a,b)
print(r,"\n")

print("1.2\n")

def foo(num):
    fn=0
    for i  in range(num):
        a=fn+i
        print(a)
        fn=i
foo(10)

print("1.3\n")

def printzuyg(str):
  for i in range(0, len(str)-1, 2):
    print(str[i])

str = "pynative"
print(" String is ", str)
printzuyg(str)

print("1.4\n")

def removen(str,n):
    return str[n:]
print("Removing n number of chars")
print(removen("pynative", 4))

print("1.5\n")
def list(nList):
    f=nList[0]
    l=nList[-1]
    if(f==l):
        return True
    else:
        return False
nList=[10,50,7,10]
print(list(nList))

print("1.6\n")

def dividedf(nlist):
    for i in nlist:
        if(i%5==0):
            print(i)

nlist=[10,8,5,30,9]
dividedf(nlist)

print("1.7\n")

str="Emma is good developer. Emma is a writer"
dubl=str.count("Emma")
print(dubl)

print("1.8\n")

for n in range(10):
    for i in range(n):
        print(n,end=" ")
    print("\n")

print("1.9\n")

def ncheck(number):
    print("original number", number)
    originalNum = number
    reverseNum = 0
    while (number > 0):
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if (originalNum == reverseNum):
        return True
    else:
        return False


print(ncheck(121))

print("1.10\n")
def chtncht(list1,list2):
    list3=[]
    for i in list1:
        if (i % 2 == 0):
            list3.append(i)
    for i in list2:
        if(i%2!=0):
            list3.append(i)
    return list3
list1=[4,55,2,88,12]
list2=[7,9,6,11,14]
print(chtncht(list1,list2))

print("1.11\n")

n=7536
while (n>0):
    d=n%10
    n=n//10
    print(d, end=" ")

    print("1.12\n")
    income = 45000
    taxPayable = 0
    print("Given income", income)

    if income <= 10000:
        taxPayable = 0
    elif income <= 20000:
        taxPayable = (income - 10000) * 10 / 100
    else:
        # first 10,000
        taxPayable = 0

        # next 10,000
        taxPayable = 10000 * 10 / 100

        # remaining
        taxPayable += (income - 20000) * 20 / 100

    print("Total tax to pay is", taxPayable)
    
print("1.13\n")
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="  ")
    print("\t\t")

print("1.14\n")

str="*"
for n in range(6,0,-1):
    for i in range(0,n-1):
        print(str, end=" ")
    print(" ")

print("1.15\n")
def pow(a, b):
    n = b
    r = 1
    while n > 0:
        r = r * a
        n = n - 1
    print(a, "raises to the power of", b, "is: ", r)


pow(5, 4)