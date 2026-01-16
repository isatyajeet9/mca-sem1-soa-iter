// a1q18
// Name: Satyajeet Nayak
// Question: Find remainder without using % operator

public class Q18_RemainderWithoutMod {
    public static void main(String[] args) {
        int a = 17, b = 5;
        int rem = a - (a / b) * b;
        System.out.println("Remainder is: " + rem);
    }
}
