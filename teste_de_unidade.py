import unittest


import main


class MyTestCase(unittest.TestCase):
    def testar_somar_dois_numeros(self):
        resultado_esperado = 40
        resultado_obtido = main.somar_dois_numeros(13, 27)
        self.assertEqual(resultado_esperado, resultado_obtido)  # Verifica a assertividade da soma


    def multiplicar_dois_numeros(mae):
        resultado_esperado1 = 15
        resultado_obtido2 = main.multiplicar_dois_numeros(4, 5)
        mae.assertEqual(resultado_esperado1, resultado_obtido2)  # Verifica a assertividade da soma



if __name__ == '__main__':
    unittest.main()
