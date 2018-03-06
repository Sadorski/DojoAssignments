def comparelists(arr1, arr2):
    if arr1 == arr2:
        print("The lists are the same")
    else:
        print("The lists are not the same")


print(comparelists([1,2,5,6,2], [1,2,5,6,2]))
print(comparelists([1,2,5,6,5], [1,2,5,6,4]))
print(comparelists([1,2,5,6,5,16], [1,2,5,6,5]))
print(comparelists(['celery','carrots','bread','milk'], ['celery','carrots','bread','cream']))
