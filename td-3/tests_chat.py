from argparse import ArgumentTypeError
import unittest
import chat

class TesterMonCat(unittest.TestCase):
    """ Classe de test. Test Chat."""
    
    def test_constructor_nominal(self):
        """Test constructeur nominal"""
        monchat = chat.Chat("Zélda", 18)
        self.assertEqual(monchat.name, "Zélda")
        self.assertEqual(monchat.classification, chat.Classification.MAMIFERE)
        self.assertIsInstance(monchat.classification, chat.Classification)
        self.assertEqual(monchat._isCute, True)
        self.assertEqual(monchat.age, 18)


    
    def test_constructor_argumenttypeerror_name(self):
        """Test constructeur ArgumentTypeError"""
        self.assertRaises(ArgumentTypeError, chat.Chat, 2, 18)
        self.assertRaises(ArgumentTypeError, chat.Chat, [1,"2",3,4], 18)
        self.assertRaises(ArgumentTypeError, chat.Chat, {"1":1 }, 18)
        self.assertRaises(ArgumentTypeError, chat.Chat, (1,2,3), 18)

    def test_constructor_argumenttypeerror_age(self):
        """Test constructeur ArgumentTypeError"""
        self.assertRaises(ArgumentTypeError, chat.Chat, "Zélda", "")
        self.assertRaises(ArgumentTypeError, chat.Chat, "Zélda", [])
        self.assertRaises(ArgumentTypeError, chat.Chat, "Zélda", {})
        self.assertRaises(ArgumentTypeError, chat.Chat, "Zélda", ())

if __name__ == '__main__':
    unittest.main()