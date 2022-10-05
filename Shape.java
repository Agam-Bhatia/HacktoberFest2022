package Oops;

public class Shape {
    public static float area(float r){
        return (float) (3.14*r*r);
    }
    public static int area(int s){
    return s*s;
    }
    public static int area(int l, int b){
        return l*b;
    }

    public static void main(String[] args) {
        System.out.println("Area of circle is: "+ area(3.5F));
        System.out.println("Area of square is: "+ area(5));
        System.out.println("Area of rectangle is: "+ area(2,3));
    }
}
