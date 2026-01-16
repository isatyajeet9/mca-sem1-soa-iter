public class Q7_SimpleCalculator {
    public static void main(String[] args) {
        int num1 = 20, num2 = 5;
        char operator = '+';
        int result = 0;

        switch (operator) {
            case '+':
                result = num1 + num2;
                System.out.println("Addition: " + result);
                break;
            case '-':
                result = num1 - num2;
                System.out.println("Subtraction: " + result);
                break;
            case '*':
                result = num1 * num2;
                System.out.println("Multiplication: " + result);
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                    System.out.println("Division: " + result);
                } else {
                    System.out.println("Cannot divide by zero");
                }
                break;
            default:
                System.out.println("Invalid operator");
        }
    }
}
