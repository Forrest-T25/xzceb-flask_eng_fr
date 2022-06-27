import unittest

from translator import englishToFrench, frenchToEnglish

class testenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(('Hello'), 'Bonjour')
        self.assertNotEqual(('Hello', null)

class testfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(('Bonjour'), 'Hello')
        self.assertNotEqual(('Bonjour', null)

unittest.main()