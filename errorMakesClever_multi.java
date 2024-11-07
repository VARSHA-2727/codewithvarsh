package errorMakesClever;
import java.util.Scanner;
public class multi {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        int a=scan.nextInt();
        int b=scan.nextInt();
        int c= scan.nextInt();
        int d=a*b*c;
        int e=a+b+c;
        System.out.println("the add num "+d);
        System.out.println("the  mul number is "+e);
        System.out.println(d/e);
    }
}
