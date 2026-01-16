// a1q6
// Name: Satyajeet Nayak
// Question: WAP to swap values of two variables without using third variable

public class Q6_SwapWithoutTemp {
    public static void main(String[] args) {
        int a = 5, b = 10;
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println("After swap: a = " + a + ", b = " + b);
    }
}
