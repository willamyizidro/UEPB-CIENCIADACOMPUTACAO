idade = int(input('Insira a idade do participante: '))
maiorIdade = 0
quantidade = 0
while idade != -1:
  sexo = int(input('Insira o sexo com 0 para masculino e 1 para feminino: '))
  olhos = int(input('Insira a cor dos olhos com 0 para azuis, 1 para verdes e 2 para castanhos: '))
  cabelos = int(input('Insira a cor dos cabelos com 0 para castanhos, 1 para loiros e 2 para pretos: '))
  if maiorIdade < idade:
    maiorIdade = idade
  if idade >= 18 and idade <= 35 and olhos == 1 and cabelos == 1 and sexo == 1:
    quantidade = quantidade + 1
  idade = int(input('Insira a idade do participante: '))
  
print('A maior idade é',maiorIdade)
print('A a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anose que tenham olhos verdes e cabelos louros é de ',quantidade)