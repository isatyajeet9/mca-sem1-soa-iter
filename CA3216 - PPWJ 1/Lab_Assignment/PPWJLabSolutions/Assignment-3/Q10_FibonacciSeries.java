public class Q10_FibonacciSeries {
    public static void main(String[] args) {
        System.out.println("First 20 terms of Fibonacci series:");
        
        int n = 20;
        long t1 = 0, t2 = 1; 
        
        System.out.print(t1 + " " + t2 + " ");
        
        for (int i = 3; i <= n; i++) {
            long sum = t1 + t2;
            System.out.print(sum+" ");
            t1 = t2;
            t2 = sum;
        }
    }
}