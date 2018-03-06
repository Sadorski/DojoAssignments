words = "It's thanksgiving day. It's my birthday, too!"
print(words.find("day")) #finds the first instance of the word Day
arr = words.split()
# print(arr)

print(min(arr)) #finds the min in the string words
print(max(arr)) #finds the max in the string words
print(arr[0], arr[-1])
arr2 = [19,2,54,-2,7,12,98,32,10,-3,6]
arr2.sort()
print(arr2)
arr3 = arr2[4:]
arr3[0] = arr2[:5]
print(arr3)
print(len(arr))
