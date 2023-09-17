tamanho = int(input('Insira o tamanho da matriz desejada: '))

def criarMatriz(tam,mat):
  for i in range(tam):
    mat.append([0] * tam)

def lerMatriz(tam,mat):
  for i in range(tam):
    for j in range(tam):
      print('M[',i+1,',',j+1,']: ',sep='',end='')
      mat[i][j] = int(input())

def imprimirMatriz(tam,mat):
  for i in range(tam):
    for j in range(tam):
      print(mat[i][j],end=' ')
    print()


matriz1 = []
soma = 0
criarMatriz(tamanho,matriz1)
print('Preencha a matriz com os valores desejados: ')
lerMatriz(tamanho,matriz1)
imprimirMatriz(tamanho,matriz1)

for i in range(tamanho):
  for j in range(tamanho):
    if i == j:
      soma = soma + matriz1[i][j]
 
print('Somando os valores da diagonal principal obtemos ',soma,)