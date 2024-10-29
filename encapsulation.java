package access;

public class encapsulation {
    private int num;
    String name;
    int[] arr;

    public int getNum() {
        return num;
    }

//    public int setNum(int num) {
//        this.num = num;
//    }

    public encapsulation( int num, String name){
            this.name = name;
            this.num = num;
            this.arr = new int[num];

        }
    }
