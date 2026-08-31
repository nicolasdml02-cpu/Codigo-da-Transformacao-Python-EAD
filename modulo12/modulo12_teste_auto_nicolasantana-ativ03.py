import unittest

class CalculadoraAvancada:
    def dividir(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Os argumentos devem ser numéricos.")
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

class TesteValidacoesEntrada(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraAvancada()

    def test_divisao_por_zero_lança_excecao(self):
        # Verifica se o erro de divisão por zero é lançado corretamente
        with self.assertRaises(ValueError) as contexto:
            self.calc.dividir(10, 0)
        self.assertEqual(str(contexto.exception), "Divisão por zero não é permitida.")

    def test_entrada_nao_numerica_lança_excecao(self):
        # Verifica validação de tipos de dados inválidos
        with self.assertRaises(TypeError):
            self.calc.dividir("10", 2)

if __name__ == '__main__':
    unittest.main()