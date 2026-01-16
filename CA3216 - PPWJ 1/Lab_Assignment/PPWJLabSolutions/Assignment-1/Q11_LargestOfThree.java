// a1q11
// Name: Satyajeet Nayak
// Question: Find largest of three numbers using relational operators

public class Q11_LargestOfThree {
    public static void main(String[] args) {
        int a = 10, b = 25, c = 20;
        int largest = (a > b && a > c) ? a : (b > c ? b : c);
        System.out.println("Largest One is: " + largest);
    }
}
