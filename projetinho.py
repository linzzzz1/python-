
import time

print('Olá, tudo bem? digite seu nome')
nome = input()
print('Digite a sua primeira nota')
nota = float(input())
print('Digite a sua segunda nota')
nota2 = float(input())
print('Digite a sua terceira nota')
nota3 = float(input())
media = (nota + nota2 + nota3) / 3
print(f"Sua média foi {media:.2f}")
time.sleep(1)
if media >= 7:
    print("Parabéns,",nome, 'você foi aprovado')

elif media >= 5:
    print('Você está de recuperação')
else:
    print('Reprovado!')

