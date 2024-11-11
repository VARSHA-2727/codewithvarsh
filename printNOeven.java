package errorMakesClever;

import java.util.Scanner;

public class printNoEven {
    public static void main(String[] args) {
        System.out.println("nu1");
        for(int i=1;i<=10;i++){
            Scanner s=new Scanner(System.in);
//            System.out.println("nu1");
            int a=s.nextInt();
            if(a%2==0){
                System.out.println("even");
            }
            else{
                System.out.println("odd");
            }
        }
    }
}
