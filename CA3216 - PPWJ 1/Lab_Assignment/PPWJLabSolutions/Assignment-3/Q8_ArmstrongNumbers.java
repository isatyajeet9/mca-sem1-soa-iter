public class Q8_ArmstrongNumbers {
    public static void main(String[] args) {
        System.out.println("Armstrong numbers between 1 and 500:");
        
        for (int num = 1; num <= 500; num++) {
            int originalNum = num;
            int sumOfCubes = 0;
            int tempNum = num;
            

            while (tempNum != 0) {
                int digit = tempNum % 10;
                sumOfCubes += (digit * digit * digit);
                tempNum /= 10;
            }
            
            
            if (sumOfCubes == originalNum) {
                System.out.println(originalNum);
            }
        }
    }
}