package errorMakesClever;
import java.util.Scanner;
public class sizeArray {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int size= s.nextInt();
        int []marks=new int [size];
        for(int i=0;i<size;i++){
            marks[i]=s.nextInt();
        }
    }
}
