#creating varible
x = 76
print(x)
"""
variable starts with letter or underscore
variable do not start with number
they only contain letter and underscore
they are case sensetive
"""
y, z = "start", "egg"
print(y)
print(z)
#output varible is seen in console window
#global variable is the variable that is outside the function.
x = "awsome"
def my_func():
    print(x)
my_func()
#local variable is the variable that is inside the function.
def my_func():
    t = "love"
    print(t)
my_func()
"""
global-key word is used to make a local function global.
"""
def fucl():
    global y2
    y2 = "meat"
fucl()
print(y2)
print("i love", y2)