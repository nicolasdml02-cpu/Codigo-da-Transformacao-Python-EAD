import unittest

class CalculadoraAvancada:
    def dividir(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Os argumentos devem ser números.")
        return a / b

class TestValidaçãoEntradas(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraAvancada()

    def test_divisao_por_zero_lança_excecao(self):
        # Verifica se lança ZeroDivisionError ao dividir por zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(10, 0)

    def test_tipo_invalido_lança_excecao(self):
        # Verifica se lança TypeError com tipos não numéricos
        with self.assertRaises(TypeError):
            self.calc.dividir("10", 2)

if __name__ == '__main__':
    unittest.main()