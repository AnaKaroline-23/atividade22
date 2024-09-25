# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
Total = 0


while True:
    número = int(input("Digite um número (0 para sair): "))
    if número == 0:
        break
    Total = número + Total


print(f'A soma total é: {Total}')

