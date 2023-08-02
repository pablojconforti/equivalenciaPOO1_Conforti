from Persona import Person
from Atleta import Athlete
from Docente import Teacher
from Planeta import Planet
from Soldado import Soldier
from Armas import Pistolete,Espadon
import unittest

class TestPlanet(unittest.TestCase):
    def setUp(self):
        self.julieta = Person(42)
        self.ana = Athlete(25)
        self.rosa = Athlete(45)
        self.rosa.tecnicas_conocidas = 8
    
        self.perla = Athlete(28)
        self.perla.tecnicas_conocidas = 4
        self.perla.masa_muscular = 6
        
        self.monica = Teacher(45)
        self.monica.cursos_dados(6)
        
        self.luisa = Teacher(35)
        self.luisa.cursos_dados(1)
        
        self.soldier1 = Soldier(30)
        self.pistolete1 = Pistolete(8)
        self.soldier1.agregar_arma(self.pistolete1)
        

        self.soldier2 = Soldier(50)
        self.pistolete2 = Pistolete(12)
        self.soldier2.agregar_arma(self.pistolete2)

        self.espadon1 = Espadon(20)
        self.soldier2.agregar_arma(self.espadon1)

        self.planet1 = Planet()
        self.planet1.agregar_habitante(self.julieta)
        self.planet1.agregar_habitante(self.ana)
        self.planet1.agregar_habitante(self.rosa)
        self.planet1.agregar_habitante(self.perla)
        self.planet1.agregar_habitante(self.monica)
        self.planet1.agregar_habitante(self.luisa)
        self.planet1.agregar_habitante(self.soldier1)
        self.planet1.agregar_habitante(self.soldier2)

    def test_construir_muralla(self):
        self.assertEqual(self.planet1.km_murallas, 0)
        self.ana.ofrecer_tributo(self.planet1)
        self.perla.ofrecer_tributo(self.planet1)
        self.assertEqual(self.planet1.km_murallas, 4)

    def test_founding_museum(self):
        self.assertEqual(self.planet1.museos, 0)
        self.monica.ofrecer_tributo(self.planet1)
        self.luisa.ofrecer_tributo(self.planet1)
        self.assertEqual(self.planet1.museos, 1)
        
    def test_poder_real(self):
        self.assertEqual(self.planet1.poder_real(),282)
        
    def test_poder_aparente(self):
        self.assertEqual(self.planet1.poder_aparente(), 496)

    def test_necesita_refuerzo(self):
        self.assertFalse(self.planet1.necesita_refuerzo())

    def test_habitantes_valiosos(self):
        habitantes_valiosos = self.planet1.habitantes_valiosos()
        self.assertEqual(len(habitantes_valiosos), 6)
        self.assertIn(self.rosa, habitantes_valiosos)
        self.assertIn(self.monica, habitantes_valiosos)
        self.assertIn(self.soldier1, habitantes_valiosos)
        self.assertIn(self.soldier2, habitantes_valiosos)

    def test_ofrecer_tributo_athlete(self):
        self.assertEqual(self.planet1.km_murallas, 0)
        self.ana.ofrecer_tributo(self.planet1)
        self.perla.ofrecer_tributo(self.planet1)
        self.assertEqual(self.planet1.km_murallas, 4)

    def test_ofrecer_tributo_teacher(self):
        self.assertEqual(self.planet1.museos, 0)
        self.monica.ofrecer_tributo(self.planet1)
        self.luisa.ofrecer_tributo(self.planet1)
        self.assertEqual(self.planet1.museos, 1)

    def test_ofrecer_tributo_soldier(self):
        self.assertEqual(self.planet1.km_murallas, 0)
        self.soldier1.ofrecer_tributo(self.planet1)
        self.soldier2.ofrecer_tributo(self.planet1)
        self.assertEqual(self.planet1.km_murallas, 10)

    def test_apaciguar_planeta(self):
        planet2 = Planet()
        self.planet1.apaciguar_planeta(planet2)
        self.assertEqual(planet2.museos, 1)
        self.assertEqual(planet2.km_murallas, 16)


if __name__ == "__main__":
    unittest.main()
