import unittest

class CalculadoraAvancada:
    def dividir(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Os argumentos devem ser números.")
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a / b

class TestValidaEntradasInvalidas(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraAvancada()

    def test_divisao_por_zero_lança_excecao(self):
        # Verifica se o erro ZeroDivisionError é levantado
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(10, 0)

    def test_entrada_nao_numerica_lança_excecao(self):
        # Verifica se o erro TypeError é levantado com entradas de texto
        with self.assertRaises(TypeError):
            self.calc.dividir("10", 2)

if __name__ == '__main__':
    unittest.main()