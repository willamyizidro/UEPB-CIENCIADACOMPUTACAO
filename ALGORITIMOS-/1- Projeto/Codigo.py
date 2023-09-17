quantidade = 10
filmes = [0] * quantidade
usuario1 = [0] * quantidade
usuario2 = [0] * quantidade
recomendacao1 = [0] * quantidade
recomendacao2 = [0] * quantidade

def inserirFilmes(quant, filmes):
  for i in range(quantidade):
    print('Insira o ',i+1,'º Filme da lista: ')
    filmes[i] = input('')

def assistiu(quant, usuario):
  print('Vou mostrar os filmes do nosso serviço digite "s" se já assistiu e se não digite "n"')
  for i in range(quant):
    print('voce ja assistiu ',filmes[i],'?')
    usuario[i] = input('')
    if usuario[i] == 'n' or usuario[i] == 'N':
      usuario[i] = False
    else:
      usuario [i] = True

def comparar(quant, usuario, users, recomendacao):
  for i in range(quant):
    if usuario[i] == False and users[i] == True:
      recomendacao[i] = True
    else:
      recomendacao[i] == False
def mostrarComparacao(quant, recomendacao):
  for i in range(quant):
    if recomendacao[i]:
      print(filmes[i], end=', ')
  print('')



inserirFilmes(quantidade, filmes)
print('Usuario 1')
assistiu(quantidade, usuario1)
print('Usuario 2')
assistiu(quantidade, usuario2)

comparar(quantidade, usuario1, usuario2, recomendacao1)

comparar(quantidade, usuario2, usuario1, recomendacao2)
print('Temos as Seguintes recomendações para o usuario 1')
mostrarComparacao(quantidade, recomendacao1)
print('Temos as Seguintes recomendações para o usuario 2')
mostrarComparacao(quantidade, recomendacao2)
