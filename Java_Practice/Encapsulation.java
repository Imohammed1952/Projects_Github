public class Student{
    private int studentID;
    private String studentName;
    private String collegeName;
    private String address;



    public int getStudentID() {
        return studentID;
    }

    public void setStudentID(int studentID) {
        this.studentID = studentID;
    }

    public String getCollegeName() {
        return collegeName;
    }

    public void setCollegeName(String collegeName) {
        this.collegeName = collegeName;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName){
        this.studentName = studentName;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address){
        this.address = address;
    }
}

public class Main {
    public static void main(String[] args) {
        Student student = new Student();

        student.setStudentID(12345);
        student.setStudentName("John Doe");
        student.setCollegeName("Springfield College");
        student.setAddress("123 Main St, Springfield");

        System.out.println("Student ID: " + student.getStudentID());
        System.out.println("Student Name: " + student.getStudentName());
        System.out.println("College Name: " + student.getCollegeName());
        System.out.println("Address: " + student.getAddress());
    }
}