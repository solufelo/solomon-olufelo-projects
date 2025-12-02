import java.util.Scanner;

public class MathCalc {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int number = scanner.nextInt();
        System.out.println("Enter another number: ");
        int number2 = scanner.nextInt();
        System.out.println("Enter an operation: ");
        String operation = scanner.next();
        if (operation.equals("+")){
            System.out.println(number + number2);
        } else if (operation.equals("-")){
            System.out.println(number - number2);
        } else if (operation.equals("*")){
            System.out.println(number * number2);
        } else if (operation.equals("/")){
            System.out.println(number / number2);
        } else {
            System.out.println("Invalid operation");
        }
        scanner.close();
    }
}
