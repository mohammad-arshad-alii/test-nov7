num2=8

class Test:
    #code change here
    @staticmethod
    def f1(num3):
        print(num3)
        num2=0

    def f2(num1, num2=9):
        print(num1)
    
a=Test()
a.f2(5) #should print 5
a.f1(7)

print(num2) #should print 0
