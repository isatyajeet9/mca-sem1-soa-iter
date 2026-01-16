public class Q13_ArraySumMethod {

    static int arraySum(int arr[]) {
        int s = 0;
        for (int x : arr)
            s += x;
        return s;
    }

    public static void main(String[] args) {
        int a[] = {1, 2, 3, 4, 5};
        System.out.println("Sum = " + arraySum(a));
    }
}
