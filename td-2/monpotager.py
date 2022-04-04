
from argparse import ArgumentTypeError


class Primeur():

    _nom = ""
    _potager = None

    def __init__(self, nom = "Gerard"):
        self._nom = nom
        print("bonjour je m'appelle %s " % self._nom)

    def entreDansUnPotager(self, potager):
        if isinstance(potager, Potager) == False:
            raise ArgumentTypeError

        self._potager = potager

    def sortDunPotager(self):
        self._potager = None

    def plante(self, fruitOuLegume):
        if isinstance(self._potager, Potager) == False:
            raise ArgumentTypeError

        self._potager._plante(fruitOuLegume)

    def ajouteZone(self, zone):
        if isinstance(self._potager, Potager) == False:
            raise ArgumentTypeError

        self._potager._ajouteZone(zone)
            
class Zone():

    _largeur = 0
    _longueur = 0

    def __init__(self, largeur, longueur):
        self._largeur = largeur
        self._longueur = longueur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, largeur):
        self._largeur = largeur

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self, longueur):
        self._longueur = longueur

class Potager(Zone):
    _zones = []

    def __init__(self, largeur, longueur):
        super().__init__(largeur, longueur)

    def _plante(self, fruitOuLegume):
        if isinstance(fruitOuLegume, (Fruit, Legume)) == False:
            raise ArgumentTypeError
        
        zoneLegume = list(filter(lambda z: isinstance(z, ZoneLegumes), self._zones))
        zoneFruit = list(filter(lambda z: isinstance(z, ZoneFruits), self._zones))

        if isinstance(fruitOuLegume, Fruit) and len(zoneFruit) > 0:
            zoneFruit[0]._fruits.append(fruitOuLegume)
            print("fruit %s ajouté dans la zone %s" % (fruitOuLegume._nom, zoneFruit[0]._nom))
            return
        
        if isinstance(fruitOuLegume, Legume) and len(zoneLegume) > 0:
            zoneLegume[0]._legumes.append(fruitOuLegume)
            print("legume %s ajouté dans la zone %s" % (fruitOuLegume._nom, zoneLegume[0]._nom))
            return

        raise Exception("instance %s non ajoutée, la zone n'existe pas!" % fruitOuLegume._nom)

    def _ajouteZone(self, zone):
        if isinstance(zone, Zone) == False:
            raise ArgumentTypeError
        
        if len(self._zones) >= 2:
            raise Exception('trop de zones !')

        if len(self._zones) == 0:
            self._zones.append(zone)
            print("zone %s ajoutée" % zone._nom)
            return
        
        filtered = filter(lambda z: isinstance(z, type(zone)), self._zones)
        if len(list(filtered)) > 0:
            raise Exception('meme zone en cours d\'ajout! %s' % type(zone))
        else:
            self._zones.append(zone)
            print("zone %s ajoutée" % zone._nom)

class ZoneLegumes(Zone):
    _nom = "Mes Legumes"
    _legumes = []

    def __init__(self, largeur, longueur):
        super().__init__(largeur, longueur)

class ZoneFruits(Zone):
    _nom = "Mes Fruits"
    _fruits = []

    def __init__(self, largeur, longueur):
        super().__init__(largeur, longueur)

class Fruit():

    def __init__(self, nom):
        self._nom = nom
        print("fruit %s créé avec succès!" % self._nom)

class Legume():

    def __init__(self, nom):
        self._nom = nom
        print("légume %s créé avec succès!" % self._nom)


### MAIN ###
if __name__ == '__main__':
    primeur = Primeur()

    monPremierPotager = Potager(50, 50)
    primeur.entreDansUnPotager(monPremierPotager)


    maPremiereZoneFruit1 = ZoneFruits(10, 10)
    primeur.ajouteZone(maPremiereZoneFruit1)

    maPremiereZoneLegume1 = ZoneLegumes(10, 10)
    primeur.ajouteZone(maPremiereZoneLegume1)

    patate = Legume("patate")
    radis = Legume("radis")
    carotte = Legume("carotte")
    
    mangue = Fruit("mangue")
    
    primeur.plante(mangue)
    primeur.sortDunPotager()
