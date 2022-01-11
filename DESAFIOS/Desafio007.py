Semestre01 = int(input("Digite a nota do semestre 1:"))
Semestre02 = int(input('Digite a nota do semestre 2:'))
Semestre03 = int(input('Digite a nota do semestre 3:'))
Media= (Semestre01 + Semestre02 + Semestre03) /2
if Media >= 40:  
    Resposta = 'Parabéns você foi aprovado'
else:
    Resposta= 'Infelizmente você está reprovado'  
print("A media do aluno nos semestre foi de {}, {} ".format(Media, Resposta)   )