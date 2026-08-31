import unittest

# Classe Calculadora
class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        return a / b

# Testes para a classe Calculadora
class TesteCalculadora(unittest.TestCase):

    def setUp(self):
        # Instancia a calculadora antes de cada teste
        self.calc = Calculadora()

    def test_metodo_somar(self):
        resultado = self.calc.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_metodo_dividir(self):
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5.0)

if __name__ == '__main__':
    unittest.main()