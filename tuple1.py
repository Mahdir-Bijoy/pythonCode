#1
def problem1():
    var1 = tuple()
    print(var1)
#problem1()
#2
def problem2():
    var2 = tuple(("string", 1, 1.3, True))
    print(var2)
#problem()
#3
def problem3():
    var3 = tuple((1,3,4,56,6))
    x = var3[2]
    print(x)
#problem3()
#4
#5
def no5(var, item):
    y = list(var)
    y.append(item)
    x = tuple(y)
    print(x)
#no5((1,2,3,5), 9)
#6
def no6(var):
    x = str(var)
    print(x)
#no6((1,3,4,4.5, True))
#7
tuplex = ("apple",1.2,3,4,5,False)
x = tuplex[3]
y = tuplex[-4]
#print(x)
#print(y)
#8
#9
"""
mytuple = (1,2,2,3,2,3,2,1,2,2,2)
index = 0
index1 = 1
x = mytuple[index]
a = len(mytuple)
while index <= a:
    x = mytuple[index]
    while index <= a:
        if mytuple[index] == mytuple[index1]:
             print(mytuple[index1])
             index1 += 1
        else:
             continue
    index += 1
#10

def tuple(tuple2, item):
    index = 0
    item = tuple2[index]
    x = len(tuple2)
    while index <= x:
        if item in tuple2:
            print(yes)
            index +=1
        else:
            print(no)
            index += 1
tuple((1,2,3,4,4,5), 4)
"""
#11
list1 =[1,2,3,4,4,5,6]
a = tuple(list1)
#print(a)
#12
tuple1 = (1,2,3,4,5,5,9,6)
a = list(tuple1)
a.remove(9)
x = tuple(a)
#print(x)
#14
def prob():
    tuplex = ("man","orange","meat",3,4,5,5)
    a = tuplex.index(5)
    print(a)
#prob()
#15
def no15():
    tuple = ("mango", "wax","fish","rice",1,234,1233,12356)
    a = len(tuple)
    print(a)
#no15()
#16
#17
#18
def no18():
    tupleE = (1,2,3,4,4,5,55,45)
    index = 0
    index1 = -1
    a = len(tupleE)
    while index <= a:
        print(tupleE[index1])
        index1 -= 1
        index += 1
#no18()
#22
def no22():
    mylist = [(),(),(""),12,2,3,12,3,223]
    



