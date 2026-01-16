import java.util.Scanner;

class Q8_SecondLargest {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = obj.nextInt();
        int a[] = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++)
            a[i] = obj.nextInt();

        int max = a[0], second = -1;

        for (int i = 0; i < n; i++) {
            if (a[i] > max) {
                second = max;
                max = a[i];
            } else if (a[i] > second && a[i] != max) {
                second = a[i];
            }
        }

        System.out.println("Second Largest = " + second);
    }
}
