def checkerboard():
    for i in range(1, 9):
        if (i % 2) == 1:
            print ("* * * *")
        else:
            print(" * * * *")

print(checkerboard())
