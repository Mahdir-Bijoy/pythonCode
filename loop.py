def cal(number1):
    maximum = number1
    number = 1
    mul = 1
    while(number <= maximum):
        mul *= number
        number += 1
    print(mul)
#cal()
a = 2
b = 4
mul = a * b
print(a,"x",b, end ="=")
print(mul)

list = [1,2,3,3,4,4,5]
a = tuple(list)
print(a)

