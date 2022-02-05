#Coleta de dados
try:
    dado1 = float(input("Digite o primeiro número:"))
    operaçao = input('')
    dado2 = float(input("Digite o segundo número:"))
except:
    print('Ouve um erro inesperado')

#Processamento 
if operaçao == '/': 
    conta = dado1 / dado2
    print(f"O valor da conta é: {conta}")

elif operaçao == '+':
    conta = dado1 + dado2
    print(f"O valor da conta é: {conta}")

elif operaçao == '-':
    conta = dado1 + dado2
    print(f"O valor da conta é: {conta}")

elif operaçao == '*':
    conta = dado1 + dado2
    print(f"O valor da conta é: {conta}")

else:
    print('Você não selecionou umas das conta suportaveis: / * + -')

