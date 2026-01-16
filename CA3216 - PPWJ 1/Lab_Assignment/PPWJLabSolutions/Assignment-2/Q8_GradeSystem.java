public class Q8_GradeSystem {
    public static void main(String[] args) {
        char grade = 'B';
        
        switch (grade) {
            case 'A':
                System.out.println("Grade: A - Excellent");
                break;
            case 'B':
                System.out.println("Grade: B - Good");
                break;
            case 'C':
                System.out.println("Grade: C → Average");
                break;
            case 'D':
                System.out.println("Grade: D → Pass");
                break;
            case 'F':
                System.out.println("Grade: F → Fail");
                break;
            default:
                System.out.println("Invalid grade");
        }
    }
}
