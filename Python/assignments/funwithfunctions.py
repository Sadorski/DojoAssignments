def odd_even():
    for i in range(1, 2001):
        if i % 2 == 0:
            print("Number is ", i, ". This is an even number.")
        else:
            print("Number is ", i, ". This is an odd number.")

odd_even()

def multiply(arr, n):
    for i in range(len(arr)):
        arr[i] *= n
    return arr


print(multiply([2, 3, 6, 12], 3))

# def layered_multiples(multiply(arr, n)):
#     new_array = []
#     for val in arr:
#         for j in val:
#             new_array.append(1)
#
#     return new_array
#
#
# x = layered_multiples(multiply([2,4,5],3))
# print x

##code doesnt work in comment
