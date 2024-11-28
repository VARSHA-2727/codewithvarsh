package errorMakesClever;
class counter{
    static int count=0;
    int instanceclass=0;
    counter(){
        count=count+1;
        instanceclass=instanceclass+1;
    }
    void dis(){
        System.out.println("instanceNum"+instanceclass);
        System.out.println("static"+count);
    }
}
public class main {
    public static void main(String[] args) {
        counter c1=new counter();
        c1.dis();
        counter c2=new counter();
        c2.dis();
        counter c3=new counter();
        c3.dis();
    }
}
