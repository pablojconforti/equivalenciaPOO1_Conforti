from Persona import Person

class Athlete(Person):
    def __init__(self, edad):
        super().__init__(edad)
        self.masa_muscular = 4
        self.tecnicas_conocidas = 2

    #Getters and setters

    def get_poder(self):
        return super().get_poder() + self.masa_muscular * self.tecnicas_conocidas

    def es_destacado(self):
        return super().es_destacado() or self.tecnicas_conocidas > 5
    
    def get_valor(self):
        return super().get_valor()
    
    #Funciones propias

    def entrenar(self, dias):
        self.masa_muscular += dias // 5

    def aprender_tecnica(self):
        self.tecnicas_conocidas += 1

    def ofrecer_tributo(self, planeta):
        if (self.get_valor() >= 40):
            planeta.construir_muralla(2)
        self.offered_tribute = True
