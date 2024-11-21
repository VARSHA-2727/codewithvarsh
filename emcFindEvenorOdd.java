package errorMakesClever;
import java.util.Scanner;
public class find {
    void evenorodd(int num1) {
        if (num1 % 2 == 0) {
            System.out.println("the no is even");
        } else {
            System.out.println("the no is odd");
        }

    }

    public static void main(String[] args) {
        System.out.println("enter the number");
        Scanner s=new Scanner(System.in);
        int number=s.nextInt();
        find obj1=new find();
        obj1.evenorodd(number);

    }
}
