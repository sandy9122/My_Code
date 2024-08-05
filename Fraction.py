class Fract:
    def __init__(self,n,d):
        self.num= n
        self.den=d
    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    def __add__(self,other):
        t_num=self.num*other.den + other.num*self.den
        t_den=self.den*other.den
        return '{}/{}'.format(t_num,t_den)

    def __sub__(self,other):
        t_num=self.num * other.den - other.num*self.den
        t_den=self.den * other.den
        return '{}/{}'.format(t_num,t_den)

    def __mul__(self,other):
        t_num=self.num * other.num
        t_den=self.den * other.den
        return '{}/{}'.format(t_num,t_den)

    def __truediv__(self,other):
        t_num=self.num * other.den
        t_den=self.den * other.den
        return '{}/{}'.format(t_num,t_den)

