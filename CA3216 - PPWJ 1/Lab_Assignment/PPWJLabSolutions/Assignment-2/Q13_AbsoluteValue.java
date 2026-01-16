public class Q13_AbsoluteValue {
    public static void main(String[] args) {
        int num = -25;
        int abs = num;
        
        if (num < 0) {
            abs = -num;
        }
        
        System.out.println("Original number: " + num);
        System.out.println("Absolute value: " + abs);
    }
}
