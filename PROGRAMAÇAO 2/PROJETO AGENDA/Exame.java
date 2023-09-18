public class Exame{
  private String nome;
  private Paciente paciente;
  private String data;
  private String hora;

  public Exame(String nome, Paciente paciente, String data, String hora){
    this.nome = nome;
    this.paciente = paciente;
    this.data = data;
    this.hora = hora;    
  }
    public Exame(String nome, Paciente paciente){
    this.nome = nome;
    this.paciente = paciente;
    this.data = "Data ainda não marcada";
    this.hora = "Data ainda não marcada";
  }
  

public String getNome() {
	return nome;
}

public void setNome(String nome) {
	this.nome = nome;
}

public Paciente getPaciente() {
	return paciente;
}

public void setPaciente(Paciente paciente) {
	this.paciente = paciente;
}

public String getData() {
	return data;
}

public void setData(String data) {
	this.data = data;
}

public String getHora() {
	return hora;
}

public void setHora(String hora) {
	this.hora = hora;
}
  
}