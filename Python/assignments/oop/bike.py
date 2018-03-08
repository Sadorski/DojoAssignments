class Bike(object):
    miles = 0
    
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        

    def displayinfo(self):  #method display the bikes price, max speed, total miles
        print str(self.price) + " Dollars"
        print str(self.max_speed) + " Miles an hour"
        print str(self.miles) + " Total Miles ridden"



    def ride(self):     #display riding on the screen, #miles += 10
        print "I am currently riding forward. Wooooooo"
        self.miles += 10
        return self

    def reverse(self):  #display revering on the screen, -= 5 
        print "I am currently riding in reverse. AHHHHHH"
        if self.miles >= 5:
            self.miles -= 5
        return self

person1 = Bike(500, 10)
person2 = Bike(1000, 15)
person3 = Bike(1500, 20)

person1.ride().ride().ride().reverse().displayinfo()
person2.ride().ride().reverse().reverse().displayinfo()
person3.reverse().reverse().reverse().displayinfo()


#Have the first instance ride 3 times, reverse once have it displayInfo()
#Second Instance ride twice, reverse twice, have it displayInfo
#3rd instance Reverse 3 times and display Info()