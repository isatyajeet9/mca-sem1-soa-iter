// a1q9
// Name: Satyajeet Nayak
// Question: WAP to find the maximum combination of 100rs

public class Q9_CurrencyCombination {
    public static void main(String[] args) {
        int amount = 100;
        int n50, n20, n10, n5, n2, n1;
        int rem;
        n50 = amount / 50;
        rem = amount % 50;

        n20 = rem / 20;
        rem = rem % 20;

        n10 = rem / 10;
        rem = rem % 10;

        n5 = rem / 5;
        rem = rem % 5;

        n2 = rem / 2;
        rem = rem % 2;

        n1 = rem;

        System.out.println("Maximum combination of 100 rupees:");
        System.out.println("50 rupee notes: " + n50);
        System.out.println("20 rupee notes: " + n20);
        System.out.println("10 rupee notes: " + n10);
        System.out.println("5 rupee notes: " + n5);
        System.out.println("2 rupee notes: " + n2);
        System.out.println("1 rupee notes: " + n1);
    }
}
