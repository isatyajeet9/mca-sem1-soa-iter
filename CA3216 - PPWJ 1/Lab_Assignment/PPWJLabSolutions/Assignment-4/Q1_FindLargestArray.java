import java.util.Scanner;

class Q1_FindLargestArray {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = obj.nextInt();
        int a[] = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++)
            a[i] = obj.nextInt();

        int max = a[0];
        for (int i = 1; i < n; i++)
            if (a[i] > max)
                max = a[i];

        System.out.println("Largest = " + max);
    }
}
