class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight 
        self.brand = brand 
        self.status = "for sale"
    
    def sold(self):
        self.status = "sold"
        return self

    def addtax(self, tax):
        self.tax = tax 
        self.price += (self.price * self.tax)
        return self

    def defect(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.price = 0
        if self.reason == "return":
            self.status = "for sale"
        if self.reason == "used":
            self.price -= (self.price * .2)
        return self

    def display_info(self):
        print "price: {}\nitem_name: {}\nweight: {}\nbrand: {}\nstatus: {}".format(self.price, self.item_name, self.weight, self.brand, self.status)

prod1 = Product(50, "ipod", 2, "apple")
prod2 = Product(200, "galaxy", 2, "samsung")
prod3 = Product(500, "bike", 2, "motorola")
prod4 = Product(1000, "tools", 2, "apple")

prod1.addtax(.20).display_info()
prod2.sold().display_info()
prod3.defect("return").display_info()
prod4.defect("used").sold().display_info()




    