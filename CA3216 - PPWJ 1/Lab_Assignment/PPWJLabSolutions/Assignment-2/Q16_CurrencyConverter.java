public class Q16_CurrencyConverter {
    public static void main(String[] args) {
        int choice = 2;
        double rupees = 1000;  
        double result = 0;
        
        switch (choice) {
            case 1:  // Dollar
                result = rupees / 83;  
                System.out.println(rupees + " INR = " + result);
                break;
            case 2:  // Euro
                result = rupees / 90;  
                System.out.println(rupees + " INR = " + result);
                break;
            case 3:  // Japanese Yen
                result = rupees * 0.75; 
                System.out.println(rupees + " INR = " + result);
                break;
            default:
                System.out.println("Invalid choice");
        }
    }
}
