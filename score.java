package errorMakesClever;
import java.util.Scanner;
public class score {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        String name= scan.nextLine();
//        int score= scan.nextInt();
        String dept= scan.nextLine();
        int score= scan.nextInt();
        System.out.println("the name is "+name);
        System.out.println("the score is"+score/10);
        System.out.println("the dept is "+dept);

