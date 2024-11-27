package errorMakesClever;
class animal {
    String name;
    int age;
   void makeSound(){
        System.out.println("animal makes sound");
    }
}
class dog extends animal{
    String breed;

    @Override
    void makeSound() {
        System.out.println("dog barks");
    }
}
class cat extends animal{
    String color;
    void makeSound(){
        System.out.println("cat meow");
    }
    void climb(){
        System.out.println("the cat is climbing");
    }

}
public class animalKingdom {
    public static void main(String[] args) {
//        animal ob1=new animal();
//        ob1.name="xcv";
//        ob1.age=23;
//        ob1.makeSound();
//
        cat c1=new cat();
//        c1.name="gimmy";
//        System.out.println(c1.name);
        c1.makeSound();
        c1.climb();
    }


}
