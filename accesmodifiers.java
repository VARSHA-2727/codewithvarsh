package errorMakesClever;
class person1{
    public String name;
    protected int age;
    private String socnum;
    String address;
    person1(){

    }
    person1(String name){
        this.name=name;
    }
    class emp1 extends person1{

    }

}
public class codingChallange {
    public static void main(String[] args) {
        person1 p1=new person1("anan");
        System.out.println(p1.name);
    }
}
