
import time

print('Olá! seja bem vindo(a)')
time.sleep(1)
tentativas = 3
while tentativas > 0:
    usuario = input('Digite seu Usuário!: ').lower()
    senha = input('Digite sua Senha!: ')
    if usuario == "admin" and senha == "1234":
        print("Logado com sucesso!")
        while True:
            print('Olá, seja bem vindo, por favor escolha uma opção:')
            print('1 - Conta bancária')
            print('2 - Histórico de compras')
            print('3 - Vendas do mês')
            print('4 - Em Desenvolvimento')
            opçao = input()
            if opçao == '1':
                print('Geregotango')
                break
            elif opçao == '2':
                print('Geregotilho')
                break
            elif opçao == '3':
                print('Geregotildo')
                break
            elif opçao == '4':
                print('Geregovaldo')
                break
            else:
                print('Por favor tente novamente')
    else:
        print("Usuário ou senha incorretas!")
        tentativas = tentativas - 1
        if tentativas == 0:
            print('Banido')
        else:
            print(f'Tentativas restantes: {tentativas}')


