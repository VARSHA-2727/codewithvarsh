package errorMakesClever;
import java.util.Scanner;
public class hw {
    public static void main(String[] args) {
        for(int i=1;i<=5;i++)
        {
            System.out.println(i);
        }
        Scanner s =new Scanner(System.in);
        System.out.println("number1");
        int a=s.nextInt();
        System.out.println("number2");
        int b=s.nextInt();
        for(int i=a;i<=b;i++){
            System.out.println(i);
        }
    }
}
