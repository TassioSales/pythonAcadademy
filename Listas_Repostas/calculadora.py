def menu():
    print(f'''{"________MENU________":^20}
    [ 1 ] SOMA 
    [ 2 ] SUBTRAÇÃO
    [ 3 ] DIVISÃO
    [ 4 ] MULTIPLICAÇÃO
    [ 5 ] POTENCIA
    [ 6 ] SAIR
    ''')
def soma(num1, num2):
    resultado = num1 + num2
    return print(f"A soma de {num1} e {num2} = {resultado}")

def subtracao(num1, num2):
    resultado = num1 - num2
    return print(f"A Subtração de {num1} e {num2} = {resultado}")

def multiplicacao(num1, num2):
    resultado = num1 * num28
    return print(f"A multiplicação de {num1} e {num2} = {resultado}")

def divisao(num1, num2):
    resultado = num1 / num2
    return print(f"A divisão de {num1} e {num2} = {resultado}")

def potencia(num1, num2):
    resultado = num1 ** num2
    return print(f"A potencia de {num1} por {num2} = {resultado:.2f}")


def calculadora(menu, soma,subtracao,multiplicacao,divisao,potencia):
    while True:
        menu()
        opc = int(input("Digite uma opção: "))
        if opc == 6:
            break
        n1 = float(input('Digite uma numero: '))
        n2 = float(input('Digite outro numero: '))
        
        if opc == 1:
            soma(n1, n2)
        elif opc == 2:
            subtracao(n1, n2)
        elif opc == 3:
            multiplicacao(n1, n2)
        elif opc == 4:
            divisao(n1, n2)
        elif opc == 5:
            potencia(n1, n2)
        else:
            return menu



calculadora(menu, soma,subtracao,multiplicacao,divisao,potencia)



