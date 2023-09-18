#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void imprimirMenu(){
  printf("Digite uma das Opções abaixo:\n");
  printf("1 - Inserir novo contribuinte.\n");
  printf("2 - Informar próximo membro a contribuir.\n");
  printf("3 - Imprimir lista completa.\n");
  printf("0 - Sair.\n\n");
}

struct no{
char nome[50];
struct no *prox;
};
typedef struct no No;

No* inserir(No* lista, char *valor){
  No* novo;
  novo = (No*) malloc(sizeof(No));
  strcpy(novo->nome, valor);
  
  if(lista == NULL){
  novo->prox = NULL;
   return novo;
  }else{
    No *pont = lista;
    
  
  while(pont->prox != NULL){
      pont = pont->prox;
    }
  novo->prox = NULL;
  pont->prox = novo;
  
  return lista;
    }
 
}

No* retirar(No*lista){
  No* p= lista;
  inserir(lista,p->nome);
  lista = p->prox;

  return lista;
}

void imprimir(No*lista){
  No*p;
  int cont = 1;
  printf("Lista atualizada dos Membros:\n");
  for(p=lista; p!=NULL; p = p->prox){
    printf("O %dº da lista é %s\n",cont, p->nome);
    cont++;
  }
  printf("\n");
}

int main(void) {

No* listaClube = NULL;
char membroNovo[50];
printf("CLUBE DO CAFÉ DOS FUNCIONARIOS.\n\n\n");  

int menu;
imprimirMenu();
scanf("%d",&menu);

  while (menu != 0) {
    switch (menu) {

    case 1:
      printf("Digite o nome do novo membro do clube:\n");
      scanf("%s",membroNovo);
      listaClube = inserir(listaClube, membroNovo);
      printf("\n");
      break;
    
    case 2:
      if(listaClube->nome == NULL){
        printf("a lista esta vazia ou possui apenas um membro.\n ");
        }else{
        printf("O proximo membro que vai comprar o café é %s\n\n",listaClube->nome);
        listaClube = retirar(listaClube);
        }
      break;

    case 3:
      imprimir(listaClube);
      break;

    default:
      printf("Opção invalida, selecione alguma opção disponivel: \n");
    }
    imprimirMenu();
    scanf("%d", &menu);
    printf("\n");
  }

printf("saiu");
  
}