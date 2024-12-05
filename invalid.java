package errorMakesClever;

import org.w3c.dom.ls.LSOutput;

import java.util.Scanner;

class invalidAgeException extends Exception{
    public invalidAgeException(String message){
        super(message);
    }
}
class agevalidator{
    void checkage(int age)
    {
        try {
            if (age < 0 || age > 150) {
                throw new invalidAgeException("age is invalid");
            }
            else{
                System.out.println("valid........");
            }
        }
            catch(Exception e){
                System.out.println(e);

            }

        }
    }
public class invalid {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
       int age=s.nextInt();
       agevalidator a1=new agevalidator();
       a1.checkage(age);
    }
}
