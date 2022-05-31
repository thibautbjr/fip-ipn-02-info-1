from argparse import ArgumentError, ArgumentTypeError
from enum import Enum


class Tailleboisson(Enum):
    Large = 0
    Medium = 1
    Small = 2


class Boisson():
    _type = Tailleboisson.Large

    def __init__(self, type):
        self._type = type

    @property
    def type(self):
        return self._type


class Carte():
    _nom = ""
    _prix = 5
    _ingrédients = list()

    def __init__(self, nom, prix, ingrédients):
        self._nom = nom
        self._prix = prix
        self._ingrédients = ingrédients

    @property
    def nom(self):
        return self._nom

    @property
    def ingrédients(self):
        return self._ingrédients

    @property
    def prix(self):
        return self._prix


class Barman():
    _Cartecommande = list()
    _Boissonselectionnee = None
    _Tailleboissonchoisie = list()
    _estPayee = False
    _estValidee = False

    @property
    def facture(self):
        total = 0
        prix = 3
        for boisson in self._Tailleboissonchoisie:
            if boisson.type == Tailleboisson.Large:
                total += (prix+1)
            elif boisson.type == Tailleboisson.Medium:
                total += (prix+0.5)
            elif boisson.type == Tailleboisson.Small:
                total += prix
            else:
                raise ArgumentTypeError("Tailleboisson inconnu!")

        return total

    @property
    def estAnnulee(self):
        return self._Boissonselectionnee == None and self._Tailleboissonchoisie == []

    @property
    def estValide(self):
        return self._Boissonselectionnee != None and len(self._Tailleboissonchoisie) > 0

    @property
    def estPayee(self):
        return self._estPayee

    @property
    def estValidee(self):
        return self._estValidee

    def __init__(self, Cartecommande):
        if isinstance(Cartecommande, list):
            if not all(isinstance(elem, Carte) for elem in Cartecommande):
                raise ArgumentTypeError("must be a list of Carte!")
        else:
            raise ArgumentTypeError("must be a list!")

        self._Cartecommande = Cartecommande

    def consultercartecommande(self):
        return self._Cartecommande

    def selectionnerBoisson(self, boisson, ingredients):
        if not isinstance(boisson, Carte):
            raise ArgumentTypeError("boisson must be a Carte!")
        if not isinstance(ingredients, str):
            raise ArgumentTypeError("ingrédients must be a string!")

        self._Boissonselectionnee = (boisson, ingredients)
        return True

    def selectionnertaille(self, boissons):
        if isinstance(boissons, list):
            if not all(isinstance(elem, Boisson) for elem in boissons):
                raise ArgumentTypeError("must be a list of Boisson!")
        else:
            raise ArgumentTypeError("must be a list!")

        self._Tailleboissonchoisie = boissons
        return True

    def valider(self):
        if self.estValide:
            self._estValidee = True
        else:
            self._estValidee = False
        return self._estValidee

    def annulerCommande(self):
        self._Tailleboissonchoisie = list()
        self._Boissonselectionnee = None
        self._estPayee = False
        self._estValidee = False

    def payer(self, somme):
        if not self.estValidee:
            raise BaseException("command must be confirmed!")

        reste = somme - self.facture
        if reste < 0:
            self._estPayee = False
        else:
            self._estPayee = True
        return (self._estPayee, reste)

    def donnerboisson(self):
        if not self.estValidee or not self.estPayee:
            raise BaseException("command must be confirmed and payed!")

        return True


if __name__ == '__main__':
    initcarte = [
        Carte("The Boost", 5, ["0.5Mango", "2 Oranges", "1 Guajana"]),
        Carte("The Fresh", 4, ["3 apples", "1 ginger", "1 lemon"]),
        Carte("The Fusion", 5, ["1 Guava", "0.75 pinapple", "0.5 Banana"]),
        Carte("The Detox", 3.5, ["3 Carrots", "1 Celery Stick", "1 Beetrout"])
    ]

    # init barmen
    barmen= Barman(initcarte)
    print("Le barmen est prêt a vous servir!")

    # consultation
    boissons = barmen.consultercartecommande()
    print("consultation de la carte:")
    for boisson in boissons:
        print("- %s : %s / %s€" % (boisson.nom, ", ".join(ingre for ingre in boisson.ingrédients), boisson.prix))

    # selection boisson
    boisson = boissons.pop(0)
    ingredients = boisson.ingrédients.pop()
    boissonchoisie = barmen.selectionnerBoisson(boisson, ingredients)
    print("L'acheteur a séléctionné sa boisson ? %s" % boissonchoisie)

    # selection taille de la boisson
    taille = list()
    taille.append(Boisson(Tailleboisson.Large))
    taille.append(Boisson(Tailleboisson.Small))
    tailleSelectionne = barmen.selectionnertaille(taille)
    print("L'acheteur a séléctionné sa taille ? %s" % tailleSelectionne)

    # validation
    estValidee = barmen.valider()
    print("commande validee ? %s" % estValidee)

    # payer
    (estPayee, reste) = barmen.payer(20)
    print("commande payee (rendu de la monnaie: %d euros) ? %s" % (reste, estPayee))

    # servirboisson
    Boissonservie = barmen.donnerboisson()
    print("boissons servies au client  ? %s" % Boissonservie)
