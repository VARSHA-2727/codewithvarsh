package errorMakesClever;
interface printablee{
    void dis();
}
interface showablee{
    void dis();
}
class sh implements printablee,showablee{
    @Override
    public void dis() {
        System.out.println("class sh");

    }
}
public class c{
    public static void main(String[] args) {
        sh c1=new sh();
        c1.dis();
    }
}
