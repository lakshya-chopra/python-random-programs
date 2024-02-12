from math import sqrt

class Point:

    def __init__(self,x:int,y:int):

        self.x = x
        self.y = y

    def print_details(self):

        print(f"the x-coord is {self.x}, and the y-coord is {self.y}")

    @classmethod
    def distance(cls,obj1,obj2):

        if isinstance(obj1,cls) and isinstance(obj2,cls):

            distance = sqrt((obj2.x - obj1.x)**2 + (obj2.y - obj1.y)**2)

            print('the distance b/w the 2 points is:',distance)
            return



p1 = Point(10,20)
p2 = Point(20,30)

p1.print_details()
p2.print_details()

Point.distance(p1,p2)
