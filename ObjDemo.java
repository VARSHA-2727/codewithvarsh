package access;

public class objDemo {
    int val;
    float gpa;

    public objDemo(int val, float gpa) {
        this.val = val;
        this.gpa = gpa;
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }

    @Override
    protected void finalize() throws Throwable {
        super.finalize();
    }

    @Override
    public String toString() {
        return super.toString();
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    public static void main(String[] args) {
        objDemo obj = new objDemo(34, 34.5f);
        objDemo obj2 = new objDemo(34, 56.7f);
        if (obj == obj2) {
            System.out.println("yes they r equal");
        }
        if (obj.equals(obj2)) {
            System.out.println("yes they r equal");
//        System.out.println(obj.hashCode());
        }
        System.out.println(obj.getClass());
    }
}
