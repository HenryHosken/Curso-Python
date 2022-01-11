Altura= float(input('Qual é a altura da parede ?'))
Largura= float(input('Qual é a largura da parede ?'))
Area= Altura * Largura
Tinta= Area / 2
Gasto = Tinta / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m² e terá o gasto de {:.2f} litros de tinta.'.format(Altura, Largura, Area, Gasto))