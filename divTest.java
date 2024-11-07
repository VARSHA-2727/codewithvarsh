package errorMakesClever;
import java.util.Scanner;
public class div3Nd5 {
    public static void main(String[] args) {
        System.out.println("enter the number");
        Scanner scan=new Scanner(System.in);
        int num=scan.nextInt();
        if(num%3==0&&num%5==0)
        {
            System.out.println("it is div by 3 and 5");
        }
        else{
            System.out.println("it is not div");
        }

    }
}
