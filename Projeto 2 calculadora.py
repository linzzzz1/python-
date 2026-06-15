

import time

print('Olá, eu sou uma calculadora, e vou fazer as suas contas')
time.sleep(1)
numero1 = float(input('Digite o primeiro valor: '))
numero2 = float(input('Digite o segundo valor: '))
while True:
    operação = (input('Digite a operação: + - * /:'))
    if operação == '+':
        print(f'seu resultado é:',numero1 + numero2)
        break
    elif operação == '-':
        print(f'seu resultado é:',numero1 - numero2)
        break
    elif operação == '*':
        print(f'seu resultado é:',numero1 * numero2)
        break
    elif operação == '/':
        if numero2 == 0:
                print('é igual a 0')
                break
        else:
            print(f'seu resultado é:',numero1 / numero2)
            break

    else:
        print('Operação inválida')
