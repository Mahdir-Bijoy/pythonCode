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
#no((1,2,3,5), 9)
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
mytuple = (1,2,2,3,2,3,2,1,2,2,2
x = mytuple[index]
a = len(mytuple)
index = 0
index1 = 1
while index <= a:
    x = mytuple[index]
    while index <= a:
        if mytuple[index] ==mytuple[index2]:
             print(mytuple[index1])
             index1+= 1
        else:
             continue
    index += 1



