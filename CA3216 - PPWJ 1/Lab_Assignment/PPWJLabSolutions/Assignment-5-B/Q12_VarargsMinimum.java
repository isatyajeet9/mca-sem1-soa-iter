public class Q12_VarargsMinimum {

    static int fun(int... a) {
        int min = a[0];
        for (int x : a)
            if (x < min) min = x;
        return min;
    }

    public static void main(String[] args) {
        System.out.println(fun(5, 2, 9, 1, 7));
    }
}
