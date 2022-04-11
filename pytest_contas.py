import pytest
import main
import csv

lista_para_multiplicar = [
    (2, 3, 6),
    (0, 4, 0),
    (-5, -3, 15),
    (8, 1000, 8000)
]

@pytest.mark.parametrize('numero1, numero2, resultado_esperado', lista_para_multiplicar)
def testmultiplicar_dois_numeros(numero1, numero2, resultado_esperado):
    # Configura - vira da lista
    # Executa
    resultado_obtido = main.multiplicar_dois_numeros(numero1, numero2)

    # Valida
    assert resultado_esperado == resultado_obtido


# Exemplo de operação por CSV.
def ler_dados_csv():
    dados_csv = []  # criamos uma lista vazia
    nome_arquivo = 'C:\\Users\\Particular\\PycharmProjects\\133livros\\vendors\\massa_dividir_dois_numeros.csv'
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            campos = csv.reader(arquivo_csv, delimiter=';')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')


@pytest.mark.parametrize('id, numero1, numero2, resultado_esperado, tipo_teste', ler_dados_csv())  # Ler Arquivo CSV
def testdividir_dois_numeros(id, numero1, numero2, resultado_esperado, tipo_teste):  # Trigger para rodar teste

    # Executa
    resultado_obtido = main.dividir_dois_numeros(int(numero1), int(numero2))

    # Valida
    if tipo_teste == 'positivo':
        assert float(resultado_esperado) == resultado_obtido
    else:
        assert resultado_esperado == resultado_obtido

# TDD

def teste_calcular_area_quadrado():
    # Configura/Prepara
    lado = 3
    resultado_esperado = 9

    # Executa
    resultado_obtido = main.calcular_area_quadrado(lado)

    # Valida
    assert resultado_esperado == resultado_obtido


def teste_calcular_area_retangulo():
    # Configura/Prepara
    largura = 5
    comprimento = 4
    resultado_esperado = 20

    # Executa
    resultado_obtido = main.calcular_area_retangulo(largura, comprimento)

    # Valida
    assert resultado_esperado == resultado_obtido


def teste_calcular_area_triangulo():
    # Configura/Prepara
    largura = 10
    comprimento = 5
    resultado_esperado = 25

    # Executa
    resultado_obtido = main.calcular_area_triangulo(largura, comprimento)

    # Valida
    assert resultado_esperado == resultado_obtido