# 1 - Bibliotecas
import unittest  # Framework de teste unitário
import main  # Referência ao arquivo Main.py


# 2 - Classes (Grupo de definições )
class CasoDeTeste(unittest.TestCase):
    # 3 - métodos e funções

    def testar_multiplicar_dois_numeros(self):
        # A - Configuração (valores de entrada)
        numero1 = 4
        numero2 = 8
        resultado_esperado = 32

        # B - Executa
        resultado_obtido = main.multiplicar_dois_numeros(numero1, numero2)
        self.assertEqual(resultado_esperado, resultado_obtido)  # Compara valores e retorna verdadeiro ou falso.

    def testar_somar_dois_numeros(self):
        numero1 = 7
        numero2 = 8
        resultado_esperado = 15
        resultado_obtido = main.somar_dois_numeros(numero1, numero2)
        self.assertEqual(resultado_esperado, resultado_obtido)


if __name__ == '__main__':
    unittest.main()
