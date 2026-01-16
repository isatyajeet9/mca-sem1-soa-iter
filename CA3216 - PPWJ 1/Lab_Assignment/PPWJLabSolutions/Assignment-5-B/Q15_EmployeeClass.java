import java.util.Scanner;

class Employee {
    int id;
    String name;
    double salary;

    void get(int i, String n, double s) {
        id = i;
        name = n;
        salary = s;
    }

    void show() {
        System.out.println(id + "  " + name + "  " + salary);
    }
}

public class Q15_EmployeeClass {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Employee e[] = new Employee[3];

        for (int i = 0; i < 3; i++) {
            e[i] = new Employee();
            System.out.print("Enter id name salary: ");
            e[i].get(sc.nextInt(), sc.next(), sc.nextDouble());
        }

        System.out.println("\nEmployee Details:");
        for (Employee emp : e)
            emp.show();
    }
}
