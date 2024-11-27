package errorMakesClever;
class person{
    String name;
    void Person(String name){
        this.name=name;
    }
}
class emp extends person{
    emp(String name){
        System.out.println(name);

    }
}
public class mainClass {
    public static void main(String[] args) {
        emp e1=new emp("john");

    }
}
