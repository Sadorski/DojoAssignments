def evenlysplit(arr):
    for i in range(0, len(arr) - 1):
        if len(arr[i]) % 2 == 0:
            for j in range(i + 1, len(arr) + 1):
                temp = arr[j-1]
                arr[j - 1] = arr[j]
                arr[j] = temp 
        arr.pop()
        i -= 1

evenlysplit(["hello", "my", "Friend", "what", "its", "ups"])