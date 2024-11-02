package interfaces;

public class car implements engine,brake,media {
    @Override
    public void start() {
        System.out.println("i start like a normal car");

    }

    @Override
    public void stop() {
        System.out.println("i stop like a normal car");

    }

    @Override
    public void brake() {
        System.out.println("i start like a normal car");

    }

    @Override
    public void acc() {
        System.out.println("i accelarate like a normal car");

    }
}
