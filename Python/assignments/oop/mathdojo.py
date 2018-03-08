class MathDojo(object):
    def __init__(self):
        self.sum = 0
    def add(self, *nums):
        self.num = 0
        for num in nums:
            if type(num) == int:
                self.num += num
            elif type (num) == list:
                for x in num:
                    self.num += x 
            elif type(num) == tuple:
                self.num += sum(num)
        self.sum += self.num
        
        return self
    
    def subtract(self, *subs):
        self.sub = 0
        for sub in subs:
            if type(sub) == int:
                self.sub += sub
            elif type(sub) == list:
                for y in sub:
                    self.sub += y
            elif type(sub) == tuple:
                self.sub += sum(sub)
        self.sum -= self.sub
        return self
    
    def result(self):
        print self.sum

md = MathDojo()
md.add([2]).add([2,5]).subtract([1,2], 3).result()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, (2,3), [1.1,2.3]).result()