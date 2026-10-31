public interface animal{
    void sound();
}

public class dog implements animal {
    String name;
    int age;

    @Override
    void sound(){
        System.out.println("Woof")
    }
}

public class cat implements animal{
    String name;
    int age;

    @Override
    void sound(){
        System.out.println("Meow")
    }

}






public interface Scannable{
    void scan(String word);
}

public interface Printable{
    String print();
}

public class Printer implements Scannable, Printable{
    String doc;

    public Printer(){
        doc = " ";
    }

    @Override
    void scan(String words){
        doc = words;
    }

    @Override
    String print(){
        return doc;
    }
}