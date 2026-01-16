public class Q6_AreaOverloading {

    static double Area(double r) {
        return Math.PI * r * r;
    }

    static double Area(double l, double b) {
        return l * b;
    }

    static double Area(double b, double h, boolean triangle) {
        return 0.5 * b * h;
    }

    public static void main(String[] args) {
        System.out.println("Circle: " + Area(5));
        System.out.println("Rectangle: " + Area(4, 6));
        System.out.println("Triangle: " + Area(4, 5, true));
    }
}
