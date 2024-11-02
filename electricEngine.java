package interfaces;

public class ElectricEngine implements engine{
    @Override
    public void start() {
        System.out.println("teh electric engine is started");

    }

    @Override
    public void stop() {
        System.out.println("the electric engine is stopped");
    }

    @Override
    public void acc() {
        System.out.println("the acc is frm ee");

    }
}
