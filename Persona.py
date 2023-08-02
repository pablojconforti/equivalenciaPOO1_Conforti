class Person:
    def __init__(self, edad):
        self.edad = edad

    #Getters and setters

    def es_destacado(self):
        return self.edad in [25, 35]

    def get_inteligencia(self):
        if (20 <= self.edad <= 40):
            return 12
        else:
            return 8

    def get_poder(self):
        return 20
    
    def get_valor(self):
        return self.get_poder() + self.get_inteligencia()