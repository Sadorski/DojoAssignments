def findchar(arr, letter):
    newlist = []
    for val in arr:
        if val.count(letter) > 0:
            newlist.append(val)
    print(newlist)

print(findchar(['hello', 'world', 'my', 'name', 'is', 'Sultan'], 'o'))
