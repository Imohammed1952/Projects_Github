public class Bank{
    double interestRate;

    public Bank(){
        interestRate = -1;
    }

    double getInterestRate(){
        return interestRate;
    }
}

public class SBI_Bank extends Bank{

    public SBI_Bank(){
        interestRate = 0.08; // Example interest rate for SBI Bank
    }
}

public class ICIC_Bank extends Bank{

    public ICIC_Bank(){
        interestRate = 0.07; // Example interest rate for ICIC Bank
    }
}

public class AXIS_Bank extends Bank{

    public AXIS_Bank(){
        interestRate = 0.09; // Example interest rate for AXIS Bank
    }
}

public class Main{
    public static void main(String[] args){
        SBI_Bank sbi  = new SBI_Bank();
        System.out.println("SBI Bank Interest Rate: " + sbi.getInterestRate());
        ICIC_Bank icic = new ICIC_Bank();
        System.out.println("ICIC Bank Interest Rate: " + icic.getInterestRate());
        AXIS_Bank axis = new AXIS_Bank();
        System.out.println("AXIS Bank Interest Rate: " + axis.getInterestRate());
    }
}