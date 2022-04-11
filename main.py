
def dizer_oi(name):
    print(f'Olá, {name}')


def somar_dois_numeros(numero1, numero2):
    return numero1 + numero2


def multiplicar_dois_numeros(numero1, numero2):
    return numero1 * numero2


def subtrair_dois_numeros(numero1, numero2):
    return numero1 - numero2


def dividir_dois_numeros(numero1, numero2):
    try:   # Tente Fazer
        return numero1 / numero2
    except ZeroDivisionError:
        return 'divisao por zero'    # Tratamento de erro


def calcular_area_quadrado(lado):
    return lado*lado


def calcular_area_retangulo(largura, comprimento):
    return comprimento*largura


def calcular_area_triangulo(largura, comprimento):
    return (comprimento * largura) / 2


if __name__ == '__main__':  # Code Trigger

    dizer_oi('Brunno')
    # soma dos numeros
    numero1 = 2
    numero2 = 3
    resultado = somar_dois_numeros(numero1, numero2)
    print(f'\nA soma de {numero1} e {numero2} é igual a {resultado}')


# multiplicar dois numeros
    resultado = multiplicar_dois_numeros(3, 5)
    print(f'\nO resultado da multiplicação é {resultado}')


# subtrair dois numeros
    resultado = subtrair_dois_numeros(100, 50)
    print(f'\nO resultado da subtração é {resultado}')

# dividir dois numeros
    resultado = dividir_dois_numeros(100, 50)
    print(f'\nO resultado da divisão é {resultado}')
