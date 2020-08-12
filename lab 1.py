#1
def read_a_number():
    a = int(input("enter a number ="))
    print(a)
#read_a_number()
#2
def myfunction():
    a = int(input("enter a number ="))
    b = int(input("enter a number ="))
    x = a + b
    y = a * b
    z = b - a
    print(x)
    print(y)
    print(z)
#myfunction()
#3
def circle():
    r = int(input("enter a number ="))
    circumference = 2*3.1416*r
    area = 3.1416*r
    print(circumference)
    print(area)
#circle()
#4
def function():
    a = int(input("enter a number ="))
    b = int(input("enter a number ="))
    if a > b:
        print(first)
#function()
#5
def no5():
    a = int(input("enter a number ="))
    b = int(input("enter a number ="))
    if a > b:
        print("first is greater")
    else:
        print("first is not greater")
#no5()
#6
def no6():
    a = int(input("enter a number ="))
    b = int(input("enter a number ="))
    if a > b:
        print("first is greater")
    elif b < a:
        print("second is greater")
    else:
        print("they are equal")
#no6()
#7
def no7():
    a = int(input("enter the larger number ="))
    b = int(input("enter the smaller number ="))
    x = a - b
#no7()
# 8
def no8():
    a = int(input("enter a number ="))
    b = a % 2
    if b == 0:
        print("even")
    else:
        print("odd")
#no8()34
#9
def no9():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)
    print(10)
#no9()
#10
def no10():
    print(2)
    print(4)
    print(6)
    print(8)
    print(10)
    print(12)
    print(14)
    print(16)
    print(18)
    print(20)
#no10()
#11
def no11(a,b,c,d,e):
    x = a + b + c + d + e
    y = int(x /5)
# not a fan of float.
    print(y)
#no11(1,2,3,4,5)
#12
def no12():
    n = int(input("enter a number = "))
    x = n(n + 1)/ 2
    print(x)
#no12()
#13
def no13(a,b,c,d,e):
    mylist = [a,b,c,d,e]
    for i in mylist:
        if i % 2 == 0:
            print("even")
        else:
            print("odd")
no13(2,4,6,9,10)

   


