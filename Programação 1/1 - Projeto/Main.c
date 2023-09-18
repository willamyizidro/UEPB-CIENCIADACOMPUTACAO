#include <stdio.h>
#include <stdlib.h>

// FUNÇÃO QUE IMPRIME O MENU DE OPÇÕES
void imprimir_menu() {
  printf("Selecione alguma função:\n");
  printf("1- Inserir dados.\n");
  printf("2- Ordenar dados.\n");
  printf("3- Imprimir dados.\n");
  printf("4- Realizar Busca.\n");
  printf("0- Sair.\n");
}

// FUNÇÃO PARA INSERIR ELEMENTOS NO VETOR
void inserir_dados(int *vet, int tam) {
  int i;
  for (i = 0; i < tam; i++) {
    printf("Digite um valor para a posição %d:", i + 1);
    scanf("%d", &vet[i]);
    ;
  }
  printf("\n");
}

// ORDENAÇÃO POR SELECTION SORT
void ordenar_vetor(int *vet, int tam) {

int menor, i, j, aux;

  for (int i = 0; i < tam - 1; i++) {
    menor = i;
    for (int j = i + 1; j < tam; j++) {
      if (vet[menor] > vet[j]) {
        menor = j;
      }
      if (i != menor) {
        aux = vet[i];
        vet[i] = vet[menor];
        vet[menor] = aux;
      }
    }
  }
}

// FUNÇÃO PARA REALIZAR A BUSCA BINARIA
int realizar_busca(int vet[], int tam, int chave) {
  int inf = 0;
  int sup = tam - 1;
  int meio;

  while (inf <= sup) {
    meio = (inf + sup) / 2;
    if (chave == vet[meio]) {
      return meio;
    } else if (chave < vet[meio]) {
      sup = meio - 1;
    } else {
      inf = meio + 1;
    }
  }
  return -1;
}

//FUNÇÃO PARA IMPRIMIR VETOR
void imprimir_vetor(int vetor[], int tamanho) {
  if (tamanho == 1) {
    printf(" O %dº elemento é: %d\n ", tamanho, vetor[tamanho - 1]);
  } else {
    imprimir_vetor(vetor, tamanho - 1);
    printf("O %dº elemento é: %d\n ", tamanho, vetor[tamanho - 1]);
  }
}

int main(void) {

  int *vetor;
  int tamanho, menu, tam;
  int i, j, b, n;
  int contador = 0;
  int busca;
  
imprimir_menu();
scanf("%d", &menu);

  while (menu != 0) {
    switch (menu) {

    case 1:
      printf("Quantos numeros deseja inserir? \n");
      scanf("%d", &tamanho);
      vetor = malloc(sizeof(int) * tamanho);
      inserir_dados(vetor, tamanho);
      printf("\n");
      break;
    
    case 2:
      ordenar_vetor(vetor, tamanho);
      printf("vetor ordenado com sucesso!");
      printf("\n\n");
      break;

    case 3:
      imprimir_vetor(vetor, tamanho);
      printf("\n \n");
      break;

    case 4:
      printf("Digite o numero que deseja buscar:\n");
      scanf("%d", &busca);
      b = realizar_busca(vetor, tamanho, busca);
      if (b != -1) {
        printf("\nNumero encontrado na %dº posicao!\n\n", b + 1);
      } else {
        printf("\nNumero não encontrado, tente novamente com outro numero.\n\n");
      }
      break;

    default:
      printf("Opção invalida, selecione alguma opção disponivel: \n");
    }
    imprimir_menu();
    scanf("%d", &menu);
    printf("\n");
  }

printf("saiu");

return 0;
}