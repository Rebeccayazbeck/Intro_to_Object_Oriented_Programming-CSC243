from function import *



class Equation :
    def __init__ (self, a  , b , c ):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getDiscriminant(self):
        delta = float(self.getB())**2 - 4*float(self.getA())*float(self.getC())
        return (delta)
    
    def getRoot1(self):
        self.getDiscriminant()
        if self.getDiscriminant() < 0:
            return 0
        else :
            r1 = ( - float(self.getB()) + (float((self.getB()))**2 - 4 * float(self.getA())* float(self.getB()))**1/2)/2 * float(self.getA())
            return r1

    def getRoot2(self):
        self.getDiscriminant()
        if self.getDiscriminant() < 0:
            return 0
     
        r2 = - ( - float(self.getB()) - (float((self.getB()))**2 - 4 * float(self.getA())* float(self.getB()))**1/2)/2 * float(self.getA())
        return r2