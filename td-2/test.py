import unittest
import chat

def importone():
    return 1

class testclasse(unittest.TestCase):
    def testConstructeur(self):
        monchat=chat.Chat("Felix")
        self.assertEqual(monchat._classification,name,)

