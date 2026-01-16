public class Q5_MaxOverloading {

    static int max(int a, int b) {
        return a > b ? a : b;
    }

    static float max(float a, float b) {
        return a > b ? a : b;
    }

    static double max(double a, double b) {
        return a > b ? a : b;
    }

    public static void main(String[] args) {
        System.out.println(max(5, 9));
        System.out.println(max(5.3f, 2.8f));
        System.out.println(max(10.2, 8.6));
    }
}
