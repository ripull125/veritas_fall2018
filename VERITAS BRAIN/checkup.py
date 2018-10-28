
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n
print(gcd(20,10))

class Fraction(object):

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom
    def show(self):
        print(self.num, "/", self.den)
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum/common,newden/common)
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    def getNum(self, myfraction):
        print(myfraction.num)
    def getden(self, myfraction):
        print(myfraction.den)
    def __mul__(self, myf, other):
        newnum = myf.num*other.num
        newden = myf.den*other.den
        print(newnum, "/", newden)
    def __gt__(self, myf, other):
        newnum = self.num*otherfraction.den > self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        print (newnum)
    def __ge__(self, myf, other):
        newnum = self.num*other.den > self.den*other.num
        newnum2 = self.num*other.den == self.den*other.num
        if newnum == True or newnum2 == True:
            newnum = True
        else:
            newnum = False
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        print (newnum)
    def __lt__(self, myf, other):
        newnum = self.num*other.den < self.den*other.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        print (newnum)
    def __ne__(self, myf, other):
        newnum = self.num*other.den != self.den*other.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        print (newnum)
    def __le__(self, myf, other):
        newnum = self.num*other.den<self.den*other.num
        newnum2 = self.num*other.den == self.den*other.num
        if newnum == True or newnum2 == True:
            newnum = True
        else:
            newnum = False
            newden = self.den * otherfraction.den
            commom = gcd(newnum, newden)
            print(newnum)

myfraction = Fraction(7,9)
otherfraction = Fraction(10,12)
myfraction.show()
print(myfraction)
print(myfraction + otherfraction)
print(myfraction == otherfraction)
myfraction.getNum(myfraction)
myfraction.getden(myfraction)
myfraction.__mul__(myfraction,otherfraction)
myfraction.__gt__(myfraction, otherfraction)
myfraction.__lt__(myfraction, otherfraction)
myfraction.__ge__(myfraction, otherfraction)
myfraction.__ne__(myfraction, otherfraction)
myfraction.__le__(myfraction, otherfraction)
