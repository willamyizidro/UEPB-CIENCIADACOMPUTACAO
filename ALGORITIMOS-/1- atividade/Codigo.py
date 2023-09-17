lados = int(input('Digite a quantidade de lados do Polígono : '))

if lados == 3:
  print ('TRIÂNGULO')
  base = float(input('Informe a base do triangulo em cm: '))
  altura = float(input('Informe a altura do triangulo em cm: '))
  area = (base * altura) / 2
  print ('a área do triangulo é:' ,area, 'cm²')
elif lados == 4:
  print('QUADRADO')
  lado = float(input('Informe o valor do lado em cm: '))
  area = lado * lado
  print ('a área do quadrado é:' ,area, 'cm²')
elif lados == 5:
  print('PENTÁGONO')
elif lados < 3:
  print('NÃO É UM POLÍGONO')
else:
  print ('POLÍGONO NÃO IDENTIFICADO')