"""
food = ["burger", "pizza", "pasta", "kebab", 1]
#print(Country[0], Country[1], Country[2], Country[3], food[-1], food[-2], food[-3], food[-4], food[-5])

Country.remove("USA")
Country.remove("UK")
Country.remove("GERMANY")
#print(Country)


numlist = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 5, 10]
def comp(number):

    if number in numlist:
        print("found")
        position= numlist.index(number)
        print(position)
    else:
        print("not found")
        numlist.append(number)
        print(numlist)

comp(8)
"""
cricket = {
    "name1" : "sakib",
    "name2" : "tamim",
    "name3" : "rahi"
}
print(cricket["name1"])
print(cricket.get("name3"))
    

