class Vektor3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"((self.x), (self.y), (self.z))"
    
    def __add__(self, other):
        return Vektor3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vektor3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __div__(self, other):
        return Vektor3(self.x / other.x, self.y / other.y, self.z / other.z)
    
    def __mul__(self, other):
        if type(other) == Vektor3:
            return Vektor3(self.y * other.x, self.y * other.y, self.z * other.z)
        elif type(other) == float or type(other) == int:
            return Vektor3(self.x * other, self.y * other, self.z * other)
        
    def __dot__(self, other):
        return Vektor3(self.x * other, self.y * other, self.z * other)
    
    def __cross__(self, other):
        return Vektor3(self.y*other.z - self.z*other.y), (self.z*other.x -self.x*other.z), (self.x*other.y - self.y*other.x)
    
    def __magnitude__(self, other):
        return Vektor3(self.x**2 + self.y**2 + self.z**2)**0.5
    
    def normalize(self):
        len = (self.x*2 + self.y2 + self.z2)*0.5
        return(self.x/len,self.y/len,self.z/len)
    
#---------------------------------------------------------------------
    
a = Vektor3(3, 4, 2)
b = Vektor3(2, 1, 0)

A = a * b
print("Komponentenweise Multiplikation:", A.x, A.y, A.z)

d = a.dot(b)
print("Skalarprodukt:", d)

K = a.cross(b)
print("Kreuzprodukt:", K.x, K.y, K.z)

a.normalize()
print("Nach der Normalisierung:", a.x, a.y, a.z)





    

    


    
