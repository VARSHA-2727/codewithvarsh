package errorMakesClever;
import java.util.Scanner;
public class rcb {
    public static void main(String[] args) {
        System.out.println("enter the result!");
        Scanner scan=new Scanner(System.in);
        String rcb= scan.nextLine();
        if(rcb.equals("win")){
            System.out.println("ee sala cup namdha");
        }
        else{
            System.out.println("better luck next time");
        }

    }
}
