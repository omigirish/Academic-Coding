import math
from abc import ABC,abstractmethod
class polygon(ABC):
    area=0
    volume=0
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getVolume(self):
        pass

class cube(polygon):

    def __init__(self,side):
        self.side=side

    def getArea(self):
        x=self.side
        area=6*x*x
        return area

    def getVolume(self):
        x=self.side
        volume = x*x*x
        return volume
class cone(polygon):

    def __init__(self,radius,height):
        self.radius = radius
        self.height=height

    def getArea(self):
        radius=self.radius
        height=self.height
        slantlength=math.sqrt(height*height+radius*radius)
        area = 3.14*radius*slantlength
        return area

    def getVolume(self):
        radius = self.radius
        height = self.height
        volume = 1/3*3.14*radius*radius*height
        return volume

s=float(input("Enter the side of the cube:"))
c1 = cube(s)
print("Cube.... Area="+str(c1.getArea())+" Volume= "+str(c1.getVolume()))
r=float(input("Enter the radius of the cone: "))
h = float(input("Enter the height of the cone: "))
co1=cone(r,h)
print("Cone.... Area=" + str(co1.getArea()) + " Volume= " + str(co1.getVolume()))

