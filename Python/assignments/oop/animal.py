class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health 
    
    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "Health: {}".format(self.health)


anim1 = Animal("Pig", 30)
anim1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health += 5
        return self 

doggo = Dog("butch")
doggo.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)
       

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"


dragy = Dragon("bilbo")
dragy.fly().display_health()


