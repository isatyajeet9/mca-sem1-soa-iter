// a1q8
// Name: Satyajeet Nayak
// Question: WAP to display reverse of two-digit number

public class Q8_ReverseTwoDigit {
    public static void main(String[] args) {
        int num = 45;
        int rev = (num % 10) * 10 + (num / 10);
        System.out.println("Reverse = " + rev);
    }
}
