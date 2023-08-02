from Persona import Person
from Atleta import Athlete
from Docente import Teacher
from Planeta import Planet
from Soldado import Soldier
from Armas import Pistolete,Espadón
import unittest

class TestPlanet(unittest.TestCase):
    def setUp(self):
        # Create individuals, soldiers, weapons, and planet instances
        self.julieta = Person(42)
        self.ana = Athlete(25)
        self.rosa = Athlete(45)
        self.rosa.techniques_known = 8
    
        self.perla = Athlete(28)
        self.perla.techniques_known = 4
        self.perla.muscular_mass = 6
        
        self.monica = Teacher(45)
        self.monica.courses_given = 6
        
        self.luisa = Teacher(35)
        self.luisa.courses_given = 1
        

        self.soldier1 = Soldier(30)
        self.pistolete1 = Pistolete(8)
        self.soldier1.add_weapon(self.pistolete1)
        

        self.soldier2 = Soldier(50)
        self.pistolete2 = Pistolete(12)
        self.soldier2.add_weapon(self.pistolete2)

        self.espadon1 = Espadón(20)
        self.soldier2.add_weapon(self.espadon1)

        self.planet1 = Planet()
        self.planet1.add_inhabitant(self.julieta)
        self.planet1.add_inhabitant(self.ana)
        self.planet1.add_inhabitant(self.rosa)
        self.planet1.add_inhabitant(self.perla)
        self.planet1.add_inhabitant(self.monica)
        self.planet1.add_inhabitant(self.luisa)
        self.planet1.add_inhabitant(self.soldier1)
        self.planet1.add_inhabitant(self.soldier2)

    def test_real_power(self):
        self.assertEqual(self.planet1.real_power(),282)
    def test_apparent_power(self):
    # Apparent power is the highest power (50) * number of inhabitants (8)
        self.assertEqual(self.planet1.apparent_power(), 496)


if __name__ == "__main__":
    unittest.main()
