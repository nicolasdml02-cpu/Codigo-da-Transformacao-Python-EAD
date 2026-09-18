import unittest

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

class TestSomaSimples(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(somar(-1, -1), -2)

    def test_soma_zero(self):
        self.assertEqual(somar(5, 0), 5)

if __name__ == '__main__':
    unittest.main()