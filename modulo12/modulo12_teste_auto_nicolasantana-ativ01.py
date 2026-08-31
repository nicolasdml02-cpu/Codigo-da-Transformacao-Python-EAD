import unittest

# Função a ser testada
def somar(a, b):
    return a + b

# Classe de teste utilizando unittest
class TesteSoma(unittest.TestCase):

    def test_soma_numeros_positivos(self):
        # Verifica se 2 + 3 é igual a 5
        self.assertEqual(somar(2, 3), 5)

    def test_soma_numeros_negativos(self):
        # Verifica se -1 + (-1) é igual a -2
        self.assertEqual(somar(-1, -1), -2)

    def test_soma_com_zero(self):
        # Verifica se 5 + 0 é igual a 5
        self.assertEqual(somar(5, 0), 5)

if __name__ == '__main__':
    # Executa os testes automatizados
    unittest.main()