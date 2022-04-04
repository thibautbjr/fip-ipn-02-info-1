
from argparse import ArgumentTypeError

from sympy import false


class Primeur():

    _nom = ""
    _potager = []

    def __init__(self, nom = "Gerard"):
        self._nom = nom
        print("bonjour je m'appelle %s " % self._nom)

    def plante(self, fruitOuLegume):
        raise NotImplementedError

    def arroseZone(self, zone):
        raise NotImplementedError

    def ajouteZone(self, zone):
        if isinstance(zone, Zone) == False:
            raise ArgumentTypeError
        
        if len(self._potager) >= 2:
            raise Exception('trop de zones !')

        if len(self._potager) == 0:
            self._potager.append(zone)
            print("zone %s ajoutée" % zone._nom)
            return
        
        filtered = filter(lambda z: isinstance(z, type(zone)), self._potager)
        if len(list(filtered)) > 0:
            raise Exception('meme zone en cours d\'ajout! %s' % type(zone))
        else:
            self._potager.append(zone)
            print("zone %s ajoutée" % zone._nom)
            
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
    
    maPremiereZoneFruit1 = ZoneFruits(10, 10)
    primeur.ajouteZone(maPremiereZoneFruit1)

    maPremiereZoneLegume1 = ZoneLegumes(10, 10)
    primeur.ajouteZone(maPremiereZoneLegume1)

    #maPremiereZoneFruit2 = ZoneFruits(10, 10)
    #primeur.ajouteZone(maPremiereZoneFruit2)