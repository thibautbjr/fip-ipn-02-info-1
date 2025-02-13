
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

        if self._potager is not None: 
            raise "le primeur est déjà dans un potager?!"

        self._potager = potager
        print("le primeur est entré dans un potager")

    def sortDunPotager(self):
        if self._potager is None:
            raise Exception("le primeur est déjà sorti du potager?!")

        self._potager = None
        print("le primeur est sorti d'un potager")

    def plante(self, fruitOuLegume):
        if self._potager is None:
            raise Exception("le primeur n'est pas entré dans un potager!")

        if isinstance(self._potager, Potager) == False:
            raise ArgumentTypeError

        self._potager._plante(fruitOuLegume)

    def ajouteZone(self, zone):
        if self._potager is None:
            raise Exception("le primeur n'est pas entré dans un potager!")

        if isinstance(self._potager, Potager) == False:
            raise ArgumentTypeError

        self._potager._ajouteZone(zone)
            
class Zone():
    _nom = "Undefined"
    _largeur = 0
    _longueur = 0

    def __init__(self, largeur, longueur):
        self._largeur = largeur
        self._longueur = longueur
        print("zone %s créé pour une surface de %d" % ( self.nom, self.aire))

    @property
    def nom(self):
        return self._nom

    @property
    def aire(self):
        return self.largeur * self.largeur

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
    _nom = "Potager"
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

    def _verificationAireAvantAjout(self, zone):
        if isinstance(zone, Zone) == False:
            raise ArgumentTypeError

        aireZones = 0 
        for z in self._zones:
            aireZones += z.aire

        if aireZones + zone.aire > self.aire:
            raise Exception("nous ne pouvons pas ajouter la zone, plus d'espace disponible")
        else:
            self._zones.append(zone)
            print("zone %s ajoutée!" % zone._nom)

    def _ajouteZone(self, zone):
        if isinstance(zone, Zone) == False:
            raise ArgumentTypeError
        
        if len(self._zones) >= 2:
            raise Exception('trop de zones !')

        if len(self._zones) == 0:
            self._verificationAireAvantAjout(zone)
            return
        
        filtered = filter(lambda z: isinstance(z, type(zone)), self._zones)
        if len(list(filtered)) > 0:
            raise Exception('meme zone en cours d\'ajout! %s' % type(zone))
        else:
            self._verificationAireAvantAjout(zone)

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

class Legumetest():

    def __init__(self, nom):
        self._nom = nom
        print("légume %s créé avec succès!" % self._nom)


### MAIN ###
if __name__ == '__main__':
    primeur = Primeur()

    monPremierPotager = Potager(20, 20)
    primeur.entreDansUnPotager(monPremierPotager)


    maPremiereZoneFruit1 = ZoneFruits(10, 10)
    primeur.ajouteZone(maPremiereZoneFruit1)

    maPremiereZoneLegume1 = ZoneLegumes(10, 10)
    primeur.ajouteZone(maPremiereZoneLegume1)

    primeur.sortDunPotager()
    primeur.entreDansUnPotager(monPremierPotager)

    patate = Legume("patate")
    radis = Legume("radis")
    carotte = Legume("carotte")
    
    mangue = Fruit("mangue")
    
    primeur.plante(mangue)
    primeur.sortDunPotager()
