package interfaces;

public class nice {
    private engine Engine;
    private media player = new CDplayer();

    public nice() {
        Engine = new powerEngine();
    }

    public nice(engine Engine) {
        this.Engine = Engine;
    }

    public void start() {
        Engine.start();
    }

    public void stop() {
        Engine.stop();
    }

    public void startMusic() {
        player.start();
    }

    public void stopMusic() {
        player.stop();
    }
}
