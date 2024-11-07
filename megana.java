package errorMakesClever;
import java.util.Scanner;
public class deadAndAlive {
    public static void main(String[] args) {
        System.out.println("enter megana status");
        Scanner scan=new Scanner(System.in);
        String mega=scan.nextLine();
        if(mega.equals("dead")){
            System.out.println("surya meets ramya");
        }
        else{
            System.out.println("marry mega");
        }
    }
}
