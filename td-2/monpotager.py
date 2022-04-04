
class Primeur():

    nom = ""

    def __init__(self, nom = "Toto"):
        self.nom = nom
        print("bonjour je m'appelle: " + self.nom)

# Constructeurs
primeur1 = Primeur()
primeur2 = Primeur("Popo")

