print("2.1\n")
a = int(input("Enter number "))
b = int(input("Enter number "))

print("\n")
r = a + b
print(r)

print("2.2\n")
print('My', 'Name', 'Is', 'James', sep='**')

print("2.3\n")
print('%o,' % (8))

print("2.4\n")
print('%.2f' % 458.541315)

print("2.5\n")
n = []
k= int(input("Enter the list size : "))

print("\n")
for i in range(0, k):
    print("Enter number at location", i, ":")
    item = float(input())
    n.append(item)

print(n)

print("2.6\n")
count = 0
with open("test.txt", "r") as fp:
    lines = fp.readlines()
    count = len(lines)
with open("newFile.txt", "w") as fp:
    for line in lines:
        if (count == 3):
            count -= 1
            continue
        else:
            fp.write(line)
        count-=1
print("2.7\n")

str1, str2, str3 = input("Enter 3 string").split()
print(str1, str2, str3)

print("2.8\n")
quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))

print("2.9\n")
import os
print(os.stat("test.txt").st_size == 0)

print("2.10\n")
count = 0
with open("test.txt", "r") as fp:
    lines = fp.readlines()
    print(lines[3])

