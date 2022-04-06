from argparse import ArgumentTypeError
import unittest
import chat

class TesterMonCat(unittest.TestCase):
    """ Classe de test. Test Chat."""
    
    def test_constructor_nominal(self):
        """Test constructeur nominal"""
        monchat = chat.Chat("Zélda")
        self.assertEqual(monchat.name, "Zélda")
        self.assertEqual(monchat.classification, chat.Classification.MAMIFERE)
        self.assertIsInstance(monchat.classification, chat.Classification)
        self.assertEqual(monchat._isCute, True)

    
    def test_constructor_argumenttypeerror(self):
        """Test constructeur ArgumentTypeError"""
        self.assertRaises(ArgumentTypeError, chat.Chat, 2)
        self.assertRaises(ArgumentTypeError, chat.Chat, [1,"2",3,4])
        self.assertRaises(ArgumentTypeError, chat.Chat, {"1":1 })
        self.assertRaises(ArgumentTypeError, chat.Chat, (1,2,3))

if __name__ == '__main__':
    unittest.main()