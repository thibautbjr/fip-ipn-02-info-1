from enum import Enum
from unicodedata import name
from argparse import ArgumentTypeError




class Classification(Enum):
    POISSON= 0
    INSECTE=1
    OISEAU=2
    MAMMIFERE=3
    AMPHIBIEN=4
    REPTILE=5
    INVERTEBRE=6

class Animal():
    _classification= None
    _name=""

    def __init__(self,classification,name):
        self._name=name
        self._classification=classification
    @property
    def classification(self):
        return self._classification



class chat(Animal):
    def __init__(self,name):
        super().__init__(Classification.MAMMIFERE,name)
