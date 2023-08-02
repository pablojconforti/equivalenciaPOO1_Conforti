class Pistolete:
    def __init__(self, largo_cm):
        self.largo_cm = largo_cm

    def get_poder(self, edad):
        if edad > 30:
            return self.largo_cm * 3
        else:
            return self.largo_cm * 2


class Espadon:
    def __init__(self, peso_kg):
        self.peso_kg = peso_kg

    def get_poder(self, edad):
        if edad < 40:
            return self.peso_kg / 2
        else:
            return 6
