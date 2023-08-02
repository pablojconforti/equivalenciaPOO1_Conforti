from Persona import Person

class Teacher(Person):
    def __init__(self, edad):
        super().__init__(edad)
        self.curso = 0

    #Getters and setters

    def get_inteligencia(self):
        return super().get_inteligencia() + 2 * self.curso

    def es_destacado(self):
        return self.curso > 3
    
    def cursos_dados(self,cantidad):
        self.curso=self.curso+cantidad
        
    def dar_curso(self):
        self.curso+=1

    def get_valor(self):
        return super().get_valor() + 5
    
    #Funciones propias

    def ofrecer_tributo(self, planet):
        if self.get_valor() >= 40:
            planet.crear_museo()
        self.offered_tribute = True 
        