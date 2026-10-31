import java.util.HashMap;
import java.util.Arraylist;
import java.util.HashSet;

public class main{
    public static void main(String[] args){

        Arraylist<String> names = new Arraylist<>();
        names.add("Alice")
        names.add("Bob")
        names.add("Chris")
    
        System.out.println(names.get(0));

        for (String name : names){
            System.out.println(name)
        }
    
        HashSet<Integer> numbers = new HashSet<>();
        numbers.add(10)
        numbers.add(909)
        numbers.add(10)

        System.out.println(numbers.get(0))
        System.out.println(numbers.size())

        for (Integer number : numbers){
            System.out.println{number}
        }

        HashMap<String, Integer> map = new HashMap<>();
        map.put("Alica", 22)
        map.put("boba", 32)
        map.put("Char", 34)

        System.out.println(map.get("Alica"))

        for(String name : map.keySet()){
            System.out.println(name + ": " + map.get(name))
        }

    }

}