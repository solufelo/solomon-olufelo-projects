package cp213;

/**
 * @author Solomon Olufelo - 210729170 - oluf9170@mylaurier.ca
 * @version 2025-09-28
 */
public class Strings {
    // Constants
    public static final String VOWELS = "aeiouAEIOU";

    /**
     * Determines if {@code string} is a "palindrome": a word, verse, or sentence
     * (such as "Able was I ere I saw Elba") that reads the same backward or
     * forward. Ignores case, spaces, digits, and punctuation in {@code string}.
     *
     * @param string a string
     * @return {@code true} if {@code string} is a palindrome, {@code false}
     *         otherwise
     */
    public static boolean isPalindrome(final String string) {
        // Handle null input
        if (string == null) {
            return false;
        }
        
        // Clean the string: keep only letters and convert to lowercase
        StringBuilder clean = new StringBuilder();
        for (int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if (Character.isLetter(c)) {
                clean.append(Character.toLowerCase(c));
            }
        }
        
        // Compare cleaned string with its reverse using two-pointer approach
        String cleanStr = clean.toString();
        int left = 0;
        int right = cleanStr.length() - 1;
        
        while (left < right) {
            if (cleanStr.charAt(left) != cleanStr.charAt(right)) {
                return false; // Characters don't match
            }
            left++;
            right--;
        }
        
        return true; // All characters matched
    }

    /**
     * Determines if {@code name} is a valid Java variable name. Variables names
     * must start with a letter or an underscore, but cannot be an underscore alone.
     * The rest of the variable name may consist of letters, numbers and
     * underscores.
     *
     * @param name a string to test as a Java variable name
     * @return {@code true} if {@code name} is a valid Java variable name,
     *         {@code false} otherwise
     */
    public static boolean isValid(final String name) {
        // Handle null, empty, or underscore-only cases
        if (name == null || name.isEmpty() || name.equals("_")) {
            return false;
        }
        
        // Check first character: must be letter or underscore
        char first = name.charAt(0);
        if (!Character.isLetter(first) && first != '_') {
            return false;
        }
        
        // Check remaining characters: must be letters, digits, or underscores
        for (int i = 1; i < name.length(); i++) {
            char c = name.charAt(i);
            if (!Character.isLetterOrDigit(c) && c != '_') {
                return false;
            }
        }
        
        return true; // All validation checks passed
    }

    /**
     * Converts a word to Pig Latin. The conversion is:
     * <ul>
     * <li>if a word begins with a vowel, add "way" to the end of the word.</li>
     * <li>if the word begins with consonants, move the leading consonants to the
     * end of the word and add "ay" to the end of that. "y" is treated as a
     * consonant if it is the first character in the word, and as a vowel for
     * anywhere else in the word.</li>
     * </ul>
     * Preserve the case of the word - i.e. if the first character of word is
     * upper-case, then the new first character should also be upper case.
     *
     * @param word the string to convert to Pig Latin
     * @return the Pig Latin version of word
     */
    public static String pigLatin(String word) {
        // Handle null or empty word
        if (word == null || word.isEmpty()) {
            return word;
        }
        
        // Find the first vowel position (handle 'y' special case)
        int firstVowelIndex = -1;
        for (int i = 0; i < word.length(); i++) {
            char c = Character.toLowerCase(word.charAt(i));
            
            // Check if it's a vowel (a, e, i, o, u) or 'y' not at the beginning
            if (VOWELS.toLowerCase().indexOf(c) != -1 || (c == 'y' && i > 0)) {
                firstVowelIndex = i;
                break;
            }
        }
        
        String result;
        
        if (firstVowelIndex == 0) {
            // Word starts with vowel: add "way"
            result = word + "way";
        } else if (firstVowelIndex == -1) {
            // No vowels found: treat as all consonants, add "ay"
            result = word + "ay";
        } else {
            // Word starts with consonants: move them to end and add "ay"
            String consonants = word.substring(0, firstVowelIndex);
            String remainder = word.substring(firstVowelIndex);
            result = remainder + consonants + "ay";
        }
        
        // Preserve capitalization: if original word started with capital,
        // make sure new word starts with capital and rest is lowercase
        if (Character.isUpperCase(word.charAt(0))) {
            result = Character.toUpperCase(result.charAt(0)) + 
                     result.substring(1).toLowerCase();
        }
        
        return result;
    }
}
