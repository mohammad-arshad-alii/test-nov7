class Time:
    def __init__(self, hour, min):
        self.hour = hour
        self.min = min
      
    #add code here


t1 = Time(4, 54)
t2 = Time(3, 42)
t3 = t1 + t2
print(t3) # should print "8:36"
