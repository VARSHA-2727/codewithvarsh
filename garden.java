package errorMakesClever;
import java.util.Scanner;
public class garden {
    int apple_price;
    int apply_count;
    void total() {
        System.out.println("the total is "+apply_count * apple_price);
    }

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
//        System.out.println("enter the apple price");
        garden obj1=new garden();
        System.out.println("enter the apple price");
        obj1.apple_price=s.nextInt();
        System.out.println("enter the apple count");
        obj1.apply_count=s.nextInt();
        obj1.total();
    }
}
