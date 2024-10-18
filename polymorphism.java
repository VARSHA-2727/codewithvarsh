package polymorphism;

public class numbers {
    int sum(int a,int b){
        return a+b;
    }
    int sum(int a,int b,int c){
        return a+b+c;
    }

    public static void main(String[] args) {
        numbers obj=new numbers();
        int r=obj.sum(2,5);
        System.out.println("the sum is"+r);
    }
}
