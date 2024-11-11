package errorMakesClever;
import java.util.Scanner;
public class NumFrom1to100 {
    public static void main(String[] args) {
        System.out.println("enter the numbers form 1 to 100");
        for(int i=1;i<=100;i++){
            if(i%3==0&&i%5==0){
                System.out.println(i);
            }
        }
    }
}
