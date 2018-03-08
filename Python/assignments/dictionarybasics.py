personal = {}
personal["name"] = "Sultan"
personal["age"] = 31
personal["country of birth"] = "The United States"
personal["favorite language"] = "Ruby"

def pinfo(param):
    for key,data in param.items():
        print "My {} is {}".format(key,data)
     
    

pinfo(personal)
