from argparse import ArgumentTypeError
from enum import Enum

class Classification(Enum):
    POISSON = 0
    INSECTE = 1
    OISEAU = 2
    MAMIFERE = 3
    AMPHIBIEN = 4
    REPTILE = 5
    INVERTEBRE = 6

class Animal():
    _classification = None
    _name = ""
    _age = None

    def __init__(self, name, age, classification):
        if not isinstance(name, str):
            raise ArgumentTypeError("must be a string!")

        if not isinstance(age, int):
            raise ArgumentTypeError("must be an integer!")

        if not isinstance(classification, Classification):
            raise ArgumentTypeError("must be a Classification!")

        self._name = name
        self._age = age
        self._classification = classification

    @property
    def classification(self):
        return self._classification

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class Chat(Animal):
    _isCute = True

    def __init__(self, name, age):
        super().__init__(name, age, Classification.MAMIFERE)