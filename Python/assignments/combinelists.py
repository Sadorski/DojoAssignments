def dictfromlists(list1, list2):
    if len(list1) > len(list2):
        newdict = zip(list1, list2)
        newdict = dict(newdict)
        return newdict
    else:
        newdict = zip(list2, list1)
        newdict = dict(newdict)
        return newdict
    

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "penguins"]

print dictfromlists(name, favorite_animal)