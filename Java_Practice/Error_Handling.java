public class main(){
    public static void main(Strings[] args){
        try{
            int a = 10;
            int b = 0;

            int result = a/b;
        }
        catch(ArithmeticException err){
            System.out.println("Cannot divide by zero")
        }

        System.out.println("Program continues")
    }
}


public static void checkAge(int age){
    if (age < 0){
        throw new IllegalAgeException("Must be a valid age");
    }
    else{
        System.out.println(age)
    }
}


import java.io.IOException;

public class main(){
    public void readFile(String fileName) throws IOException{
        throw new IOException("could not read file");
    };
    
    public static void main(String[] args){
        try{
            readFile();
        }
        catch(IOException err){
            System.out.println(err.getMessage());
        }
    };
}