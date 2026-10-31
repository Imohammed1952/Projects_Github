import java.util.Arraylist;
import java.utitl.list;


public interface EmployeeService{
    void addEmployee(Sting name);
    void displayEmployees();
}

class EmployeeManager extends EmployeeService{
    private list<String> employees = new Arraylist<>();

    @Override
    public void addEmployee(String name){
        if (name == null || name.isBlank()){
            throw new IlegalArguementException("invalid name");
        }
        else{
            employees.add(name);
        }
    }

    @Override
    public void displayEmployees(){
        for(String employee : employees){
            System.out.println(employee);
        }
    }
}


public class main{
    public static void main(String[] args){
        EmployeeManager manager = new EmployeeManager();

        try{
            manager.addEmployee("Alice");
            manager.addEmployee("Bob");
            manager.addEmployee("")
        }
        catch(IlegalArguementException err){
            System.out.println(err.getMessage());
        }
    }

    manager.displayEmployees;
}