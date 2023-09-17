
print ('Insira numeros entre 0  e 100 para saber quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100] ')
print('Insira um valor negativo quando quizer terminar. ')
numero = int(input('Insira um numero: '))
contador0a25 = 0
contador25a50 = 0
contador51a75 = 0
contador76a100 = 0

while numero > 0:
  if numero >=0 and numero <= 25:
    contador0a25 = contador0a25 +1
  elif numero >= 26 and numero <= 50:
    contador25a50 = contador25a50 + 1
  elif numero >= 51 and numero <= 75:
    contador51a75 = contador51a75 + 1
  elif numero >=76 and numero <=100:
    contador76a100 = contador76a100 + 1
  numero = int(input('Digite outro numero: '))
print('foram digitados ',contador0a25,'numeros entre [0-25],',contador25a50,'numeros entre [26-50],',contador51a75,'numeros entre [51-75] e',contador76a100, 'numeros entre [76-100]')