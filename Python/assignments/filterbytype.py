def checktype(param):
    if type(param) is int:
        if int(param) >= 100:
            print("That's a big number")
        else:
            print("That's a small number")
    elif type(param) is str:
        if len(str(param)) >= 50:
            print("Long Sentence")
        else:
            print("Short Sentence")
    elif type(param) is list:
        if len(param) >= 10:
            print("Big list")
        else:
            print("Short list")

print(checktype(45))
print(checktype(100))
print(checktype(455))
print(checktype(0))
print(checktype(-23))
print(checktype("Rubber baby buggy bumpers"))
print(checktype("Experience is simply the anme we give our mistakes"))
print(checktype("Tell me and I forget. Teach me and I remember.  Involve me and I learn"))
print(checktype(""))
print(checktype([1,7,4,21]))
print(checktype([3,5,7,34,3,2,113,65,8,89]))
print(checktype([4,34,22,68,9,13,3,5,7,9,2,12,45,923]))
print(checktype([]))
print(checktype(['name','address','phone number','social security number']))
