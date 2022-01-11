preço= float(input('Digite o preço do produto: '))
valor= int(input('Digite o valor do desconto: '))
ajuste= (valor / 100)
desconto= preço * (ajuste)
reajuste= preço - desconto
print('O produto custava R${:.2f}, com {}% de desconto, ficou R${:.2f}'.format(preço, valor, reajuste))