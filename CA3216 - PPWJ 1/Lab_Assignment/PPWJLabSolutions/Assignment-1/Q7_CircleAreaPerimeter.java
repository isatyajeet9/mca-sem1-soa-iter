// a1q7
// Name: Satyajeet Nayak
// Question: WAP to find area and perimeter of a circle, where diameter=20.8
// Math.PI is a constant defined in the Math class that represents the mathematical value of π (pi)

public class Q7_CircleAreaPerimeter {
    public static void main(String[] args) {
        double diameter = 20.8;
        double radius = diameter / 2;
        double area = Math.PI * radius * radius;
        double perimeter = 2 * Math.PI * radius;
        System.out.println("Area = " + area);
        System.out.println("Perimeter = " + perimeter);
    }
}
