
public class Paciente extends Pessoa{
  protected Exame exame;
  protected String medicamento;
  public Paciente(String nome, String cpf, String celular){
    super(nome,cpf,celular);
    medicamento = "";
  }
  
public Exame getExame() {
	return exame;
}
public void setExame(Exame exame) {
	this.exame = exame;
}
public String getMedicamento() {
	return medicamento;
}
public void setMedicamento(String medicamento) {
	this.medicamento = medicamento;
}

public String toString(){
  
  if(exame != null){
    String retorno = "";
    retorno = retorno + "Nome: ";
    retorno = retorno + this.nome;
    retorno = retorno + " | CPF: ";
    retorno = retorno + this.cpf;
    retorno = retorno + " | Exame prescrito: ";
    retorno = retorno + this.exame.getNome();
    retorno = retorno +" | Medicamento: ";
    retorno = retorno +this.medicamento;
    retorno = retorno +"\n";
    return retorno;
  }else return "Nome: "+this.nome+" | CPF: "+this.cpf+" | Medicamento: "+this.medicamento+"\n";
  
  
  
}  

}