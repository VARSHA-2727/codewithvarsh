public class inheritance {
    double l;
    double w;
    double h;
    inheritance(){
        this.h=-1;
        this.w=-1;
        this.l=-1;

    }
    inheritance(double l,double h,double w){
        this.h=h;
        this.w=w;
        this.l=l;
    }
    inheritance(inheritance old){
        this.h=old.h;
        this.w=old.w;
        this.l=old.l;

    }
}
