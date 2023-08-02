from Persona import Person
from Atleta import Athlete
from Docente import Teacher

class Planet:
    def __init__(self):
        self.habitantes = []
        self.museos = 0
        self.km_murallas = 0

    def agregar_habitante(self, person):
        self.habitantes.append(person)

    def agregar_museo(self):
        self.museos += 1

    def delegacion_diplomatica(self):
        return [person for person in self.habitantes if person.es_destacado()]

    def defensa_inicial(self):
        return len([person for person in self.habitantes if person.get_poder() >= 30])

    def es_culto(self):
        return self.museos >= 2 and all(person.get_inteligencia() >= 10 for person in self.habitantes)

    def poder_real(self):
        return sum(person.get_poder() for person in self.habitantes)

    def construir_muralla(self, length_km):
        self.km_murallas += length_km

    def crear_museo(self):
        self.museos += 1

    def poder_aparente(self):
        return max(person.get_poder() for person in self.habitantes) * len(self.habitantes)

    def necesita_refuerzo(self):
        return self.poder_aparente() >= 2 * self.poder_real()
    
    def habitantes_valiosos(self):
        return [person for person in self.habitantes if person.get_valor() >= 40]

    def apaciguar_planeta(self, other_planet):
        for person in self.habitantes_valiosos():
            person.ofrecer_tributo(other_planet)