package cp213;

/**
 * @author Solomon Olufelo - 210729170
 * @version 2025-09-07
 */
public class Cipher {
    // Constants
    public static final String ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public static final int ALPHA_LENGTH = ALPHA.length();

    /**
     * Encipher a string using a shift cipher. Each letter is replaced by a letter
     * {@code n} letters to the right of the original. Thus for example, all shift
     * values evenly divisible by 26 (the length of the English alphabet) replace a
     * letter with itself. Non-letters are left unchanged.
     *
     * @param string the string to encipher
     * @param n      the number of letters to shift
     * @return the enciphered string in all upper-case
     */
    public static String shift(final String string, final int n) {
        // Handle null or empty string
        if (string == null) {
            return null;
        }
        
        // StringBuilder for efficient string building
        StringBuilder result = new StringBuilder();
        
        // Convert input to uppercase for consistent processing
        String upperString = string.toUpperCase();
        
        // Process each character in the string
        for (int i = 0; i < upperString.length(); i++) {
            char currentChar = upperString.charAt(i);
            
            // Check if character is a letter (A-Z)
            if (currentChar >= 'A' && currentChar <= 'Z') {
                // Find the position of the letter in the alphabet (0-25)
                int originalPosition = currentChar - 'A';
                
                // Apply the shift with modular arithmetic to handle wrapping
                // Adding ALPHA_LENGTH before modulo ensures positive result for negative shifts
                int newPosition = (originalPosition + n % ALPHA_LENGTH + ALPHA_LENGTH) % ALPHA_LENGTH;
                
                // Convert back to character and append
                char newChar = (char) ('A' + newPosition);
                result.append(newChar);
            } else {
                // Non-letters are left unchanged
                result.append(currentChar);
            }
        }
        
        return result.toString();
    }

    /**
     * Encipher a string using the letter positions in ciphertext. Each letter is
     * replaced by the letter in the same ordinal position in the ciphertext.
     * Non-letters are left unchanged. Ex:
     *
     * <pre>
    Alphabet:   ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Ciphertext: AVIBROWNZCEFGHJKLMPQSTUXYD
     * </pre>
     *
     * A is replaced by A, B by V, C by I, D by B, E by R, and so on. Non-letters
     * are ignored.
     *
     * @param string     string to encipher
     * @param ciphertext ciphertext alphabet
     * @return the enciphered string in all upper-case
     */
    public static String substitute(final String string, final String ciphertext) {
        // Handle null inputs
        if (string == null || ciphertext == null) {
            return null;
        }
        
        // Validate ciphertext length
        if (ciphertext.length() != ALPHA_LENGTH) {
            throw new IllegalArgumentException("Ciphertext must be exactly " + ALPHA_LENGTH + " characters long");
        }
        
        // StringBuilder for efficient string building
        StringBuilder result = new StringBuilder();
        
        // Convert input to uppercase for consistent processing
        String upperString = string.toUpperCase();
        String upperCiphertext = ciphertext.toUpperCase();
        
        // Process each character in the string
        for (int i = 0; i < upperString.length(); i++) {
            char currentChar = upperString.charAt(i);
            
            // Check if character is a letter (A-Z)
            if (currentChar >= 'A' && currentChar <= 'Z') {
                // Find the position of the letter in the standard alphabet (0-25)
                int alphabetPosition = currentChar - 'A';
                
                // Replace with the character at the same position in the ciphertext
                char substitutedChar = upperCiphertext.charAt(alphabetPosition);
                result.append(substitutedChar);
            } else {
                // Non-letters are left unchanged
                result.append(currentChar);
            }
        }
        
        return result.toString();
    }
    
    // Additional helper method for testing and understanding
    public static void demonstrateCiphers() {
        System.out.println("=== CIPHER DEMONSTRATION ===\n");
        
        // Shift Cipher Examples
        System.out.println("SHIFT CIPHER EXAMPLES:");
        System.out.println("Original: 'HELLO WORLD'");
        System.out.println("Shift by 3: '" + shift("HELLO WORLD", 3) + "'");
        System.out.println("Shift by -3: '" + shift("HELLO WORLD", -3) + "'");
        System.out.println("Shift by 26: '" + shift("HELLO WORLD", 26) + "' (same as original)");
        System.out.println();
        
        // Substitution Cipher Example
        System.out.println("SUBSTITUTION CIPHER EXAMPLE:");
        String cipherAlphabet = "AVIBROWNZCEFGHJKLMPQSTUXYD";
        System.out.println("Standard:  " + ALPHA);
        System.out.println("Cipher:    " + cipherAlphabet);
        System.out.println("Original: 'HELLO WORLD'");
        System.out.println("Substituted: '" + substitute("HELLO WORLD", cipherAlphabet) + "'");
    }
    
    // Main method for testing
    public static void main(String[] args) {
        demonstrateCiphers();
    }
}
