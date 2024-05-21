class Diamond:
    def __init__(self,price,carat,cut,color,clarity,x,y,z,table):
        self.__price=price
        self.__carat=carat
        self.__cut=cut
        self.__color=color
        self.__clarity=clarity
        self.__x=x
        self.__y=y
        self.__z=z
        self.__depth=(2*z) / (x+y)
        self.__table=table
    def CalculateVolume(self):
        return self.__x*self.__y*self.__z
    def DisplayInfo(self):
        print("Price:", self.__price," Carat: ",self.__carat, "cut:",self.__cut, "color:", self.__color,
            "clarity:",self.__clarity, "Volume:", "depth:",self.__depth, "table:",self.__table)
    def GetTablePercentage(self):
        table_percentage = (self.__table / max(self.__x, self.__y)) * 100
        return  table_percentage
    def IsHighQuality(self):
        if self.__cut == "Ideal" and self.__clarity == "IF":
            return True
        return False

# d1=Diamond(600,0.3,"Ideal","D","IF",1,7,3,45)
# print(d1.isHighQuality())

