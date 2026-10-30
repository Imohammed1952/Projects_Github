public class dog{
    String breed;
    int age;
    String name;

    void bark(){
        System.out.print("Bark");
    }

    void eat(){
        System.out.print("eat");
    }

    void sleep(){
        System.out.print("sleep");
    }
}

public class Student{
    //Vars
    String name;
    int age;
    String grade;

    //Csonstructor
    public Student(){
        name = "";
        age = -1;
        grade = "";
    }

    public Student(String name, int age){
        this.name = name;
        this.age = age;
        this.grade = "";
    }

    //Methods
    void display(){
        System.out.print("Name: " + name + ", Age: " + age + ", Grade: " + grade);
    }
}

public class Teacher{

    public int id;
    private int grade;
    private String name; 

    public Teacher(int id, int grade, String name){
        this.id = id;
        this.grade = grade;
        this.name = name;
    };

    public Teacher(){
        id = -1;
        grade = -1;
        name = "N/A"
    };

    public int getGrade(){
        return grade;
    };

    public void setName(int Name){
        this.Name = Name;
    };

    public int getName(){
        return Name;
    };

    public void setName(int Name){
        this.Name = Name;
    };

    void display(){
        System.out.println("Teacher with Id: " + id + " Name: " + name + " Grade: " + grade)
    };

}

public class TeacherAssitant extends Teacher{
    private int yearsWorked;

    public int getYearsWorked{
        return yearsWorkedl
    }l

    public void setYearsWorked(int yearsWorked){
        this.yearsWorked = yearsWorkedl
    }l

    void display(){
        System.out.println("Teacher Assistant with Id: " + id + " Name: " + name " Grade: " + grade + " Years Worked: " + yearsWorked)l
    }l
}