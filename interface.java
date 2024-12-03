package errorMakesClever;

import org.w3c.dom.ls.LSOutput;

interface readable{
    void read();
}
interface writable{
    void write();
}
interface storable{
    void store();
}
class file implements readable,writable,storable{
    @Override
    public void read() {
        System.out.println("reading........");

    }

    @Override
    public void write() {
        System.out.println("write......");
    }

    @Override
    public void store() {
        System.out.println("store.......");
    }
}
public class sm {
    public static void main(String[] args) {
        file f1=new file();
        f1.write();
        f1.read();
        f1.store();
    }
}
