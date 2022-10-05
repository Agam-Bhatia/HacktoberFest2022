package Oops;

import java.util.Scanner;

public class SumOfDigitsOfInteger {
    public static int sum(int a){
        int r;
        int sum1=0;
        int temp=a;
        while(a>0){
            r=a%10;
            sum1=sum1+r;
            a=a/10;
        }
        return sum1;
    }

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter a number: ");
        int x= s.nextInt();

        System.out.println("sum of digits of " +x+ " is: "+sum(x));
    }
}
