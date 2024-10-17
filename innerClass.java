public class inner {
    static class test {
        String name;

        public test(String name) {
            this.name = name;
        }
    }
    public static void main(String[] args) {
        test a=new test("varsha");
        test b=new test("rahul");
        System.out.println(a.name);
        System.out.println(b.name);
    }
}
