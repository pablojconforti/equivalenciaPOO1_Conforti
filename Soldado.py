from Persona import Person

class Soldier(Person):
    def __init__(self, edad):
        super().__init__(edad)
        self.armas = []

    #Getters and setters

    def get_valor(self):
        return super().get_valor()
    
    def get_poder(self):
        poder = super().get_poder()
        arma_power = sum(arma.get_poder(self.edad) for arma in self.armas)
        return poder + arma_power

    #Funciones propias

    def agregar_arma(self, arma):
        self.armas.append(arma)

    def ofrecer_tributo(self, planet):
        if (self.get_valor() >= 40):
            planet.construir_muralla(5)
        self.offered_tribute = True    