import java.util.Scanner;

class Bank {
    int accNo;
    String name;
    double bal;

    void create(int a, String n, double b) {
        accNo = a;
        name = n;
        bal = b;
    }

    void deposit(double amt) {
        bal += amt;
    }

    void withdraw(double amt) {
        if (bal >= amt)
            bal -= amt;
        else
            System.out.println("Insufficient Balance");
    }

    void display() {
        System.out.println(accNo + " " + name + " " + bal);
    }
}

class Q14_BankClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Bank ob = new Bank();
        ob.create(101, "Rahul", 5000);

        int ch;
        do {
            System.out.println("1.Deposit 2.Withdraw 3.Display 4.Exit");
            ch = sc.nextInt();
            switch (ch) {
                case 1:
                    ob.deposit(sc.nextDouble());
                    break;
                case 2:
                    ob.withdraw(sc.nextDouble());
                    break;
                case 3:
                    ob.display();
                    break;
            }
        } while (ch != 4);
    }
}
