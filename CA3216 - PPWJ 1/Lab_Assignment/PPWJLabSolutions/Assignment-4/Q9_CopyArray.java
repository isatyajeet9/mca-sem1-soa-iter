import java.util.Scanner;

class Q9_CopyArray {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = obj.nextInt();
        int a[] = new int[n];
        int b[] = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++)
            a[i] = obj.nextInt();
        for (int i = 0; i < n; i++)
            b[i] = a[i];

        for (int i = 0; i < n; i++)
            System.out.print(b[i] + " ");
    }
}
