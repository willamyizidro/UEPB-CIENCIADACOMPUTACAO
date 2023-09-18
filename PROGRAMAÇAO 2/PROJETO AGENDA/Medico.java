import java.util.ArrayList;
  
public class Medico extends Pessoa{
  protected String crm;
  protected ArrayList<Consulta> agenda = new ArrayList();
  
  public Medico(String nome,String cpf, String celular, String crm){
    super(nome,cpf,celular);
    this.crm = crm;
  } 
  
public String getCrm() {
	return crm;
}
public void setCrm(String crm) {
	this.crm = crm;
}

public ArrayList<Consulta> getAgenda() {
	return agenda;
}

public void setAgenda(ArrayList<Consulta> agenda) {
	this.agenda = agenda;
}

public boolean retirarAgenda(Paciente paciente){
  for (Consulta consultas : agenda){
    if (paciente.getCpf().equals(consultas.getPaciente().getCpf())){
      this.agenda.remove(paciente);
      return true;
    }
  }
  return false;
}  

public void realizarConsulta(Paciente paciente, String exame, String medicamento ){
  
  if(retirarAgenda(paciente)){
    if(!medicamento.equals("")){
  paciente.setMedicamento(medicamento);
    }
      if (!exame.equals("")){
        Exame exameAux = new Exame(exame,paciente);
        paciente.setExame(exameAux);
        System.out.println("Exame prescrito para o paciente, solicite a marcação de data com a recepcionista!\n");
    }
  System.out.println("Consulta realizada com sucesso!\n");
  }else{
    System.out.println("Não foi encontrado agendamento para o paciente!\n");
  }
  
}  

}