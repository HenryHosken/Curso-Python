Salario=float(input('Valor atual do salario do funcionario:'))
Aumento=int(input('Porcentagem de aumento:'))
Aumento= (Salario * (Aumento / 100))
NovoSalario= Salario + Aumento
print('O funcionario recebeu um aumento de R${:.2f}, seu salario passará a ser R${} no proximo pagamento.'.format(Aumento,NovoSalario))