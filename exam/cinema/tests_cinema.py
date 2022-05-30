from argparse import ArgumentTypeError
import unittest
import cinema

class TesterMaBorne(unittest.TestCase):
    """ Classe de test. Test Borne."""
    
    def test_constructor_nominal(self):
        """Test constructeur nominal"""
        borne = cinema.Borne([])
        self.assertEqual(borne.consulterSeance(), [])

        initSeance = [
          cinema.Film("Die Hard", "affiche de die hard", ["12:40", "16:00", "20:30"]),
          cinema.Film("Maman j'ai rate l'avion", "affiche de maman j'ai rate l'avion", [
             "11:00", "13:10", "15:50", "19:00"])
        ]

        borne = cinema.Borne(initSeance)
        self.assertEqual(borne.consulterSeance(), initSeance)

    def test_contructor_argumenttypeerror(self):
        """Test constructeur ArgumentTypeError"""
        self.assertRaises(ArgumentTypeError, cinema.Borne, [2, 18])
        self.assertRaises(ArgumentTypeError, cinema.Borne, [cinema.Film("Die Hard", "affiche de die hard", ["12:40", "16:00", "20:30"]), "Heat"])
        self.assertRaises(ArgumentTypeError, cinema.Borne, ["Le Seigneur des Anneaux", "Heat"])

    def test_contructor_typeerror(self):
        """Test constructeur TypeError"""
        self.assertRaises(TypeError, cinema.Borne, "Top Gun", "Indiana Jones")
        

if __name__ == '__main__':
    unittest.main()