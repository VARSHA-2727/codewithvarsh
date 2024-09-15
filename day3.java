//array and index
package com.varsh;

import java.time.LocalDate;
import java.util.Scanner;

public class day3 {
    public static void main(String[] args) {
//        int [] number={1,2,3,4,5};
//        int five=number[4];
//        System.out.println(five);
//        for(int i =0;i<number.length-1;i++){
//            System.out.println(number[i]);
        String[] name = {"shreyas", "don", "anna", "rey"};
        for (String names : name) {
//            System.out.println(name[i]);
//            continue;
            if (names.startsWith("s")) {
                continue;
            }
            System.out.println(name);

        }
        int count = 21;
//    while(count<=20) {
//        System.out.println("count="+count);
//        count++;
//        do {
//            System.out.println(count);
//
//        }
//        while (count < 20);
//            System.out.println("DONE");
        Scanner scanner = new Scanner(System.in);
        System.out.println("enter a name");
        String username = scanner.nextLine();
        System.out.println("hello " + username);
        System.out.println("enter the age");
        int age = scanner.nextInt();
        int year = LocalDate.now().minusYears(age).getYear();
        if (age >= 18) {
            System.out.println("ur adult");
        } else {
            System.out.println("ur child");
        }
        System.out.println("you are born in" + year);
    }
}
