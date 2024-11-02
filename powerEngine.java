package interfaces;

public class powerEngine implements engine{
    @Override
    public void stop() {
        System.out.println("the engine is stpoed");

    }

    @Override
    public void start() {
        System.out.println("the engine is started");

    }

    @Override
    public void acc() {
        System.out.println("the acc is normal");

    }

}
