import math

class Figur:
 def __init__(self):
    self.name = "Figur"

 def Umfang(self):
    return 0

 def __str__(self):
    return self.name
 
class Kreis(Figur):
    def __init__(self, name, Umfang):
        super().__init__("Kreis")
        self.name = name
        self.U = Umfang

    def Umfang(self):
        return 2 * math.pi * self.radius

class Rechteck(Figur):  
    def __init__(self, name, Umfang):
        super().__init__("Dreieck")
        self.name = name
        self.U = Umfang

    def Umfang(self):
        a = abs(self.A[0] - self.B[0])
        b = abs(self.B[1] - self.C[1])
        return 2 * (a + b)

class Dreieck(Figur):
    def __init__(self, name, Umfang):
        super().__init__("Dreieck")
        self.name = name
        self.U = Umfang

    def Umfang(self):
      perimeter = 0
      for i in range(3):
        perimeter += self.distance(self.points[i], self.points[(i + 1) % 3])

class Polygon(Figur):
    def __init__(self, name, Umfang):
        super().__init__("Dreieck")
        self.name = name
        self.U = Umfang

class Polygon(Figur):
    def __init__(self, name, Umfang):
        super().__init__("Polygon")
        self.name = "Polygon"
        self.U = Umfang


#------------------------
#"Kreis M=(2.3,4.2) r=3.4"
#"Rechteck (0,0) – (10,15)"