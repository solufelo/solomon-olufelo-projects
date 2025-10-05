package cp213;

import java.util.Scanner;

/**
 * Simple keyboard sum example for Lab 01.
 *
 * @author Your Name
 * @version 2025-09-15
 */
public class ScannerTest {
    public static void main(String[] args) {
        System.out.println("Enter a series of integers. Press 'q' to quit.");
        // Read from the keyboard.
        Scanner s = new Scanner(System.in);
        int result = 0;

        while (s.hasNextInt()) {
            result += s.nextInt();
        }

        s.close();
        System.out.println("The total is " + result);
    }
}
