from Persona import Person
from Atleta import Athlete
from Docente import Teacher
from Planeta import Planet
from Soldado import Soldier
from Armas import Pistolete,Espadon
import unittest

# Import the classes if they are in a separate file or the same file
# where you have defined the classes.

class TestPerson(unittest.TestCase):
    
    def test_julieta(self):
        julieta = Person(42)
        self.assertEqual(julieta.get_inteligencia(), 8)
        self.assertEqual(julieta.get_poder(), 20)
        self.assertFalse(julieta.es_destacado())

    def test_ana(self):
        ana = Athlete(25)
        self.assertEqual(ana.get_inteligencia(), 12)
        self.assertEqual(ana.get_poder(), 28)
        self.assertTrue(ana.es_destacado())

    def test_rosa(self):
        rosa = Athlete(45)
        rosa.tecnicas_conocidas = 8
        self.assertEqual(rosa.get_inteligencia(), 8)
        self.assertEqual(rosa.get_poder(), 52)  # (20 + 4 * 8)
        self.assertTrue(rosa.es_destacado())

    def test_perla(self):
        perla = Athlete(28)
        perla.tecnicas_conocidas = 4
        perla.masa_muscular = 6
        perla.entrenar(15)
        perla.aprender_tecnica()
        perla.aprender_tecnica()
        self.assertEqual(perla.get_inteligencia(), 12)
        self.assertEqual(perla.get_poder(), 74)  # (20 + 6 * 4)
        self.assertTrue(perla.es_destacado())

    def test_monica(self):
        monica = Teacher(45)
        monica.cursos_dados(6) 
        self.assertEqual(monica.get_inteligencia(), 20)#(8+2*6)
        self.assertEqual(monica.get_poder(), 20)
        self.assertTrue(monica.es_destacado())

    def test_luisa(self):
        luisa = Teacher(35)
        luisa.cursos_dados(1)
        self.assertEqual(luisa.get_inteligencia(), 14)#(8+2*1)
        self.assertEqual(luisa.get_poder(), 20)
        self.assertFalse(luisa.es_destacado())


class TestPlanet(unittest.TestCase):
    def test_planet_values(self):
        julieta = Person(42)
        ana = Athlete(25)
        rosa = Athlete(45)
        rosa.tecnicas_conocidas = 8
        perla = Athlete(28)
        perla.tecnicas_conocidas = 4
        perla.masa_muscular = 6
        monica = Teacher(45)
        monica.cursos_dados(6)
        luisa = Teacher(35)
        luisa.cursos_dados(1)

        planet = Planet()
        planet.agregar_habitante(julieta)
        planet.agregar_habitante(ana)
        planet.agregar_habitante(rosa)
        planet.agregar_habitante(perla)
        planet.agregar_habitante(monica)
        planet.agregar_habitante(luisa)
        planet.agregar_museo()
        planet.agregar_museo()

        self.assertEqual(planet.delegacion_diplomatica(), [ana, rosa, monica])
        self.assertEqual(planet.defensa_inicial(), 2) 
        self.assertFalse(planet.es_culto()) 
        self.assertEqual(planet.poder_real(), 184)  

        
if __name__ == "__main__":
    unittest.main()
