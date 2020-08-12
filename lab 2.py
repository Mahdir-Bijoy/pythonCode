#1
def no1(n):
    x = n % 2
    if x == 0 and n > 10:
        print(n, "is greater than 10 and even")
    if x == 0 and n < 10:
        print(n, "is less than 10 and even")
    if x != 0 and n > 10:
        print(n, "is greater than 10 and odd")
    if x != 0 and n < 10:
        print(n, "is less than 10 and odd")
#no1(1)
#2
def no2(n):
    x = n % 2
    y = n % 5
    if x == 0 or y == 0:
        print(n)
#no2(20)
#3
def no3(n):
    x = n % 2
    y = n % 5
    if x == 0 and y != 0:
        print(n)
    elif x != 0 and y == 0:
        print(n)
#no3(15)
#4
def no4(n):
    x = n % 2
    y = n % 5
    if x == 0 and y == 0:
        print(n)
#no4(10000000)
#5
def no5(n):
    x = n % 2
    y = n % 5
    if x != 0 and y != 0:
        print(n)
#no5(109)
#7
def no7(n):
    if n > 50:
        print("pass")
    else:
        print("you will not pass")
#no7(50)
#8
def no8(n):
    if n >= 90:
        print("A")
    if n >= 80 and n <= 89 :
        print("B")
    if n >= 70 and n <= 79:
        print("C")
    if n >= 60 and n <=69 :
        print("D")
    if n > 50 and n <= 59 :
        print("E")
    if n < 50:
        print("F")
#no8(95)
















