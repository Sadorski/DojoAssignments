import datetime

class Call(object):
    def __init__(self, uid, name, number, time, reason):
        self.uid = uid
        self.name = name
        self.number = number 
        self.time = datetime.datetime.strptime(time, "%I:%M%p")
        self.reason = reason
    
    def display(self):
        time = self.time.strftime
        print "Unique ID:\t{}\nCaller Name:\t{}\nCaller Phone Number:\t{}\nTime of Call:\t{}\nReason for call:\t{}".format(self.uid, self.name, self.number, time, self.reason)


call1 = Call(323, "Jim", "1111111", "3:35pm", "Internet is not working")
call2 = Call(324, "Pam", "2222222", "4:40pm", "Someone stole art supplies")
call3 = Call(325, "Ryan", "3333333", "5:00pm", "Kelly is following me")
call4 = Call(326, "Kelly", "4444444", "5:05pm", "Have you seen Ryan?")


class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue_size = len(self.calls)
    
    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self
    
    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self

    def removenumber(self, call):
        for item in range(self.queue_size - 1):
            if self.calls[item].number == call:
                self.calls.pop(item)
                self.queue_size -= 1
        return self

    def sortqueue(self):
        # for item in range(self.queue_size - 1):
        #     if self.calls[item].time < self.calls[item].time:
        self.calls = sorted(
            self.calls, key=lambda x: x.time)
        
        return self

    def info(self):
        for call in self.calls:
            print "Name:\t{}\nPhone Number:\t{}\n".format(call.name, call.number)
        print self.queue_size
        return self

        
        
test = CallCenter([call1, call2, call3, call4])
test.info().removenumber("4444444").info()
test.add(Call(232, "Creed", "6666666", "3:06pm", "Just for kicks")).info().removenumber("1111111").sortqueue().info()