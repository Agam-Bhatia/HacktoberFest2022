package Oops;

import java.util.Scanner;

public class SimpleInterest {
    public static void interest(float p, int r, int t) {
        for (int i = 1; i <= t; i++) {
            float si = (float)(p * r * t) / 100;
            System.out.println(i + "     " + si);
            p = p + si;
        }
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter principle amount: ");
        float x = s.nextInt();
        System.out.println("Enter rate of interest: ");
        int y = s.nextInt();
        System.out.println("Enter years: ");
        int z = s.nextInt();
        interest(x, y, z);
    }
}
