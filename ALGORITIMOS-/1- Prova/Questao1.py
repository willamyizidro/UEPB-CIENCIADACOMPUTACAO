nome = input('Insira o nome do atleta: ')
nota = float(input('Insira a nota do atleta: '))
menorNota = nota
maiorNota = nota
soma = nota
for i in range (6):
  nota = float(input('Insira a nota do atleta: '))
  if nota > maiorNota:
    maiorNota = nota
  if nota < menorNota:
    menorNota = nota
  soma = soma + nota
media = (soma - menorNota - maiorNota) / 5
print ('Atleta:',nome)
print ('Melhor Nota:',maiorNota)
print ('Pior Nota:',menorNota)
print ('Media:',media)
