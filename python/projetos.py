from operator import truediv
import getpass

ativo = True
logado = False
nome = input('Digite seu E-mail aqui: ')
senha = getpass.getpass('Digite sua senha: ')
#Para o "and", funcionar ambos os valores pressisam ser True

if ativo and logado:
    print(f"Bem vindo, {nome}.")
else:
    print('Ative sua conta para poder continuar...')


