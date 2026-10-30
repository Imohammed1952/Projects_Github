public class Employee{
    int salary;
    int id;

    public Employee(int salary, int id){
        this.salary = salary;
        this.id = id;
    }
}

public class Programmer extends Employee{
    int bonus;

    public Programmer(int salary, int bonus){ff
        super(salary, -1);
        this.bonus = bonus;
    }
}


class Animal{
    void eat(){
        System.out.println("Eating...");
    }
}

class Dog extends Animal{
    void bark(){
        System.out.println("Barking...");
    }
}

public class Main{
    public static void main(String[] args){
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
