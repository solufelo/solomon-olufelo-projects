package cp213;

import java.io.PrintStream;
import java.util.Scanner;

/**
 * @author Solomon Olufelo - 210729170 - oluf9170@mylaurier.ca
 * @version 2025-09-28
 */
public class SerialNumber {

    /**
     * Determines if a string contains all digits.
     *
     * @param string the string to test
     * @return {@code true} if {@code string} is all digits, {@code false} otherwise
     */
    public static boolean allDigits(final String string) {
        // Handle null or empty string
        if (string == null) {
            return false;
        }
        
        // Empty string is considered all digits (vacuous truth)
        if (string.length() == 0) {
            return true;
        }
        
        // Check each character to ensure it's a digit
        for (int i = 0; i < string.length(); i++) {
            if (!Character.isDigit(string.charAt(i))) {
                return false; // Found non-digit character
            }
        }
        
        return true; // All characters are digits
    }

    /**
     * Determines if a string is a good serial number. Good serial numbers are of
     * the form 'SN/nnnn-nnn', where 'n' is a digit.
     *
     * @param sn the serial number to test
     * @return {@code true} if the serial number is valid in form, {@code false}
     *         otherwise.
     */
    public static boolean validSn(final String sn) {
        // Handle null input
        if (sn == null) {
            return false;
        }
        
        // Check exact length requirement: SN/nnnn-nnn = 11 characters
        if (sn.length() != 11) {
            return false;
        }
        
        // Check if starts with "SN/"
        if (!sn.startsWith("SN/")) {
            return false;
        }
        
        // Check position 7 is hyphen
        if (sn.charAt(7) != '-') {
            return false;
        }
        
        // Check positions 3-6 are all digits (nnnn part)
        for (int i = 3; i <= 6; i++) {
            if (!Character.isDigit(sn.charAt(i))) {
                return false;
            }
        }
        
        // Check positions 8-10 are all digits (nnn part)
        for (int i = 8; i < sn.length(); i++) {
            if (!Character.isDigit(sn.charAt(i))) {
                return false;
            }
        }
        
        return true; // All validation checks passed
    }

    /**
     * Evaluates serial numbers from a file. Writes valid serial numbers to
     * {@code goodSns}, and invalid serial numbers to {@code badSns}. Each line of
     * {@code fileIn} contains a (possibly valid) serial number.
     *
     * @param fileIn  a file already open for reading
     * @param goodSns a file already open for writing
     * @param badSns  a file already open for writing
     */
    public static void validSnFile(final Scanner fileIn, final PrintStream goodSns, final PrintStream badSns) {
        // Process each line in the input file
        while (fileIn.hasNextLine()) {
            String line = fileIn.nextLine();
            
            // Validate the serial number and write to appropriate file
            if (validSn(line)) {
                goodSns.println(line); // Valid serial number
            } else {
                badSns.println(line);  // Invalid serial number
            }
        }
    }
}
