import random
print random.randint(60,100)


def grades():


    for i in range(10):
        rgrade = random.randint(60,100)
        if rgrade > 89:
            print "Score :",rgrade,"; Your grade is an A"
        elif rgrade > 79:
            print "Score :",rgrade,"; Your grade is a B"
        elif rgrade > 69:
            print "Score :",rgrade,"; Your grade is a C"
        else:
            print "Score :",rgrade,"; Your grade is a D"

print(grades())