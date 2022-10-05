package Oops;

class Animal1{
    void eat(){
        System.out.println("eating...");
    }
}
class Dog extends Animal1{
    void bark(){
        System.out.println("barking...");
    }
}
public class SingleInheritance {
    public static void main(String[] args) {
        Dog d= new Dog();
        d.eat();
        d.bark();
    }
}