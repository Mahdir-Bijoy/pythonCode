def displayNumber(number):
    a = 1
    while (a <= number):
        print(a)
        a += 1

#calculation(1000)
def even(n):
    a = 1
    b = a % 2
    while (a < n):
        a += 1
        b = a % 2
        if (b != 0):
            continue
        elif(b == 0):
            print(a)
#even(26)
def odd(n):
    a = 1
    b = a % 2
    while (a < n):
        b = a % 2
        if (b != 0):
            print(a)
            a += 1
        else:
            a += 1
            continue
#odd(10)
def reverse_list(mylist):
    index = -1
    a = mylist[index]
    b = len(mylist)
    while (index >= -b):
        a = mylist[index]
        print(a)
        index -= 1
#reverse_list([1,2,3,4])
def print_odd_item(list):
    index = 0
    x = list[index]
    y = len(list)
    a = x % 2
    while (index <= y):
        x = list[index]
        a = x % 2
        if (a != 0):
            print(x)
            index += 1
        else:
            index += 1
            continue
#print_odd_item([1,2,3,5,7,9,11])
def list_type(list1):
    a = len(list1)
    b = a % 2
    if b == 0:
        print("even list")
    else:
        print("odd list")
#list_type([1,2,3,4,["six"],[4.3],7j])
def times(n):
    a = n
    b = 1
    mul = a * b
    while b <= 10:
        print(a,"x",b, end="=")
        print(mul)
        b += 1
        mul = n * b
#times(21)
def string_list(list2, item):
    if item in list2:
        print("found")
        print(list2)
    else:
        print("not found")
        a = list2.append(item)
        print(list2)

#string_list(["man","egg","house"],"women")
def function(n):
    sum = 0
    for i in range(1,n):
        sum += 1
        return sum
#function(12)
def convert(miles):
    km = 1.6 * miles
    return km
x = convert(2)
print(x)









