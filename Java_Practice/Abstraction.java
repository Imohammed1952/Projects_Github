abstract class Bank{
    abstract double getRateOfInterest();
}

class SBI_Bank extends Bank{
    double getRateOfInterest(){
        return 0.07; 
    }
}

class PNB_Bank extends Bank{
    double getRateOfInterest(){
        return 0.05;
    }
}

class Main{
    public static void main(String[] args) {
        SBI_Bank sbi = new SBI_Bank();
        System.out.println("SBI Bank Interest: " + sbi.getRateOfInterest());

        PNB_Bank pnb = new PNB_Bank();
        System.out.println("PNB Bank Interest: " + pnb.getRateOfInterest());
    }
}

abstract class Employee{
    public int id;
    private String name;
    private int salary;

    public Employee(int id, String name, int salary){
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

    public Employee(){
        id = -1;
        name = "N/A";
        salary = -1;
    }

    abstract void ping();
}

class Programmer extends Employee{

    public Programmer(int id, String name, int salary){
        super(id, name, salary)
    }

    public Programmer(){
        super()
    }

    void ping(){
        System.out.println("Ping");
    }
}