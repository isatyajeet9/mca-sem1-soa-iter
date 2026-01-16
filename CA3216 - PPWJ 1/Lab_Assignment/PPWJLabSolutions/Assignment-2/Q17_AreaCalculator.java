public class Q17_AreaCalculator {
    public static void main(String[] args) {
        int choice = 2;  
        double area = 0;
        
        switch (choice) {
            case 1:  // Circle
                double radius = 5;
                area = Math.PI * radius * radius;
                System.out.println("Area of Circle: " + area);
                break;
            case 2:  // Rectangle
                double length = 10, width = 8;
                area = length * width;
                System.out.println("Area of Rectangle: " + area);
                break;
            case 3:  // Triangle
                double base = 6, height = 7;
                area = 0.5 * base * height;
                System.out.println("Area of Triangle: " + area);
                break;
            default:
                System.out.println("Invalid choice");
        }
    }
}
