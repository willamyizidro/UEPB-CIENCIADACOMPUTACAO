massa = float(input('Insira a Massa em gramas do material radioativo: '))
tempo = 0
print('A massa inicial foi de:' ,massa,'gramas')
while massa >= 0.5:
  massa = massa / 2
  tempo = tempo + 1
tempoTotal = tempo * 50
horas = int(tempoTotal / 3600)
restoHoras = tempoTotal % 3600
minutos = int(restoHoras / 60)
segundos = int(restoHoras % 60)
print('A massa final foi de:',massa, ', e o tempo gasto foi de:',horas,'Horas,',minutos,'minutos e',segundos,'segundos')