def listtype(arr):
    Sum = 0
    string = ""
    for i in arr:
        if type(i) == (int or float):
            Sum += i
        elif type(i) == str:
            string = string + i
    if Sum != 0 and string != "":
        print("The list you entered is of a mixed type")
        print(string)
        print("Sum: ",Sum)
    elif Sum != 0 and string == "":
        print("The list you entered is of integer type")
        print("Sum: ",Sum)
    elif Sum == 0 and string != "":
        print("The list you entered is a string type")
        print(string)

print(listtype([5, 3.3, 6.0]))
print(listtype(["Harry", "Potter", "is", "Amazing"]))
print(listtype(["You", 6, "can't", 12, "stop", 3.14, "this"]))
