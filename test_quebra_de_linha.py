import unittest
from idlelib import replace


def quebrar_linha(entrada):
    nova_posicao = 0
    ultima_posicao_espaco = 0
    saida = list(entrada)

    for posicao, caracter in enumerate(entrada):
        if caracter == " ":
            ultima_posicao_espaco = posicao
        if (posicao+1) % 20 == 0:
            nova_posicao = posicao if caracter == " " else ultima_posicao_espaco
            saida[nova_posicao] = "\n"

    return "".join(saida)

class TestQuebraDeLinha(unittest.TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_1(self):
        entrada = "Um pequeno jabuti xereta viu dez cegonhas felizes."
        esperado = "Um pequeno jabuti\nxereta viu dez\ncegonhas felizes."
        self.assertEqual(esperado, quebrar_linha(entrada))

    def test_2(self):
        entrada = "Um pequeno jabuti xereta viu dez cegonhas"
        esperado = "Um pequeno jabuti\nxereta viu dez\ncegonhas"
        self.assertEqual(esperado, quebrar_linha(entrada))

if __name__ == '__main__':
    unittest.main()
