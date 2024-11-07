package errorMakesClever;
import java.util.Scanner;
public class maek {
    public static void main(String[] args) {
        System.out.println("enetr the marks");
        Scanner s =new Scanner(System.in);
        int marks=s.nextInt();
        if(marks>35){
            System.out.println("pass");
        }
        else{
            System.out.println("fail");
        }

    }
}
