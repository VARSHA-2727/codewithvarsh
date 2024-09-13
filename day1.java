package com.varsh;

import java.time.LocalDate;

public class demo {
    public static void main(String[] args) {
       int number =10;
       String band="varsha";
        LocalDate localDate = LocalDate.now();
        System.out.println(localDate);
        int a=20;
        int b=a;
         a=100;
         System.out.println(b);
         System.out.println("a="+a+",b="+b);

    }
}
