package errorMakesClever;
import java.util.Scanner;
class div{
  void divisionNum(int num,int den) {
      try{
          int result=num/den;
          System.out.println("result is"+result);
      }
      catch (ArithmeticException e){
          System.out.println("cannot divide by 0");
      }
  }
}
public class division {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int n1=s.nextInt();
        int n2=s.nextInt();
        div d1=new div();
        d1.divisionNum(n1,n2);

    }
}
