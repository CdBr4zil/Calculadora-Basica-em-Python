while True:
    try: #Verifica se o usuario não digitou algum número
        numero_1 = float(input('Digite um número: '))
        numero_2 = float(input('Digite outro número: '))
        operador = input('Escolha o operador:\nSoma (+)\nSubtração (-)\n'
                    'Multiplicação (*)\nDivisão(/)\nDigite aqui: ')
        if operador == '+':
            resultado = numero_1 + numero_2
            print('O resultado é: ', resultado)
        elif operador == '-':
            resultado = numero_1 - numero_2
            print('O resultado é: ', resultado)
        elif operador == '*':
            resultado = numero_1 * numero_2
            print('O resultado é: ', resultado)
        elif operador == '/':
            if numero_2 == 0:
                print('Erro: divisão por 0')
            else:
                resultado = numero_1 / numero_2
                print('O resultado é: ', resultado)
        else:
            print('Você digitou um operador incorreto')
    except ValueError:
        print('Você não digitou nenhum número')

    sair = input('Sair? [s]: ').lower().startswith('s') # Se o usuario quiser sair, não importa o s digitado, será retorado True e para o programa
    if sair is True:
        break
print('Fim')