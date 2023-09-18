public class Recepcionista extends Pessoa{
  String matricula;
  public Recepcionista(String nome, String cpf, String celular, String matricula){
    super(nome,cpf,celular);
    this.matricula = matricula;
    }
  
public String getMatricula() {
	return matricula;
}
public void setMatricula(String matricula) {
	this.matricula = matricula;
}

//consultar agenda do medico
public void consultaAgendaMedico(Medico medico, String data){
  boolean teste = true;
  System.out.println("Consultas agendadas para o dia: "+data);
  for (Consulta consultaAux : medico.getAgenda()){
    if (data.equals(consultaAux.getData())){
      teste = false;
      consultaAux.imprimirConsulta();
      }
  }if(teste){
    System.out.println("Não existem consultas para o dia informado\n");
  }
}

// agendar Consulta na agenda do medico
public void agendarConsulta(Medico medico, Paciente paciente, String data, String hora){
  boolean teste = true;
  for (Consulta consultaAux : medico.getAgenda()){
    if (data.equals(consultaAux.getData()) && hora.equals(consultaAux.getHora())){
      teste = false;  
      System.out.println("Erro! data e hora ja possuem agendamento!\n");
    }
  } 
  if(teste){
  Consulta consulta = new Consulta(medico,paciente,data,hora);
  medico.getAgenda().add(consulta);
  System.out.println("Consulta Adicionada com sucesso!\n");
  }
}

// imprimir agenda do medico  
public void imprimirAgendaMedico(Medico medico){
  for (Consulta consultas : medico.getAgenda()){
    consultas.imprimirAgenda();
  }
}

// imprimir agenda medico dia
public void imprimirAgendaMedicoDia(Medico medico, String data){
  for (Consulta consultas : medico.getAgenda()){
    if (data.equals(consultas.getData())){
    consultas.imprimirAgenda();
    }
  }
}

//marcar data exame
public Exame marcarDataExame(Paciente paciente, String data, String hora){
  Exame exameAux = new Exame(paciente.getExame().getNome(),paciente,data,hora);
  paciente.setExame(exameAux);
  System.out.println("Data marcada com sucesso!\n");
  return exameAux;
}

}