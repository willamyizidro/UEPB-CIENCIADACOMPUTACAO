import java.util.ArrayList;
class Main {
  public static void main(String[] args) {

    
    ArrayList<Exame> agendaExames = new ArrayList();
    ArrayList<Paciente> pacientes = new ArrayList();
    ArrayList<Medico> medicos = new ArrayList();

    //adicionando pacientes
    pacientes.add(new Paciente("Willamy","09149943448","83988004600"));
    pacientes.add(new Paciente("Damiao","99999999999","83987664455"));
    
    //adicionando medico
    medicos.add(new Medico("Vanessa","10141904445","83981496415","5241-5"));
    
    //criando recepcionista
    Recepcionista r = new Recepcionista("nome","cpf","celular","matricula");
    
    //consultando agenda medico
    r.consultaAgendaMedico(medicos.get(0),"25/12/2022");
    
    // agendando consulta medico 
    r.agendarConsulta(medicos.get(0),pacientes.get(0),"25/12/2022","10:00");
    
    // agendando consulta medico erro mesma data e hora
    r.agendarConsulta(medicos.get(0),pacientes.get(0),"25/12/2022","10:00");
    
    // agendando consulta medico 
    r.agendarConsulta(medicos.get(0),pacientes.get(1),"25/12/2022","11:00");
    r.agendarConsulta(medicos.get(0),pacientes.get(0),"26/12/2022","11:00");
    
    // medico realizar consulta
    medicos.get(0).realizarConsulta(pacientes.get(0),"Ressonancia","dipirona");
    System.out.println(pacientes.get(0).getExame().getData());
    // recepcionista marca data exame 
    agendaExames.add(r.marcarDataExame(pacientes.get(0),"22/10/2022","10:00"));
    
    //imprimir paciente
    System.out.println(pacientes.get(0));
    System.out.println(pacientes.get(1));

    //imprimir Agenda medico        
    r.imprimirAgendaMedico(medicos.get(0));
    
    //imprimir Agenda do medico em determinado dia
    r.imprimirAgendaMedicoDia(medicos.get(0),"26/12/2022");

    
    }
}