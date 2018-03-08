class Car(object):
    def __init__(self, price, speed, fuel, mileage): #price, speed, fuel, mileage. if price > 10,000 set tax to be 15 percent, else 12 percent
        self.price = price
        self.speed = speed
        self.fuel = fuel 
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()
    
    
    def display_all(self): #returns all the information about the car as a string, 
        print "Price: {}\nSpeed: {}\nFuel: {}\nMileage: {}\ntax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

person1 = Car(2000, "35mph", "Full", "15mpg")
person2 = Car(12000, "55pmh", "half-empty", "23 mpg")
