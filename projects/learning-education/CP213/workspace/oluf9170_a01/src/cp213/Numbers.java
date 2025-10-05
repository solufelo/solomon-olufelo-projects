package cp213;

/**
 * @author Solomon Olufelo - 210729170 - oluf9170@mylaurier.ca
 * @version 2025-09-28
 */
public class Numbers {

    /**
     * Determines closest value of two values to a target value.
     *
     * @param target the target value
     * @param v1     first comparison value
     * @param v2     second comparison value
     * @return one of {@code v1} or {@code v2} that is closest to {@code target},
     *         {@code v1} is the value chosen if {@code v1} and {@code v2} are an
     *         equal distance from {@code target}
     */
    public static double closest(final double target, final double v1, final double v2) {
        // Calculate absolute distances from target to each value
        double distance1 = Math.abs(target - v1);
        double distance2 = Math.abs(target - v2);
        
        // Return v1 if distances are equal (tie-breaker rule)
        // or if v1 is closer
        return (distance1 <= distance2) ? v1 : v2;
    }

    /**
     * Determines if {@code n} is a prime number. Prime numbers are whole numbers
     * greater than 1, that have only two factors - 1 and the number itself. Prime
     * numbers are divisible only by the number 1 or itself.
     *
     * @param n an integer
     * @return {@code true} if n is prime, {@code false} otherwise
     */
    public static boolean isPrime(final int n) {
        // Handle special cases
        if (n <= 1) {
            return false; // Numbers <= 1 are not prime
        }
        if (n == 2) {
            return true; // 2 is the only even prime number
        }
        if (n % 2 == 0) {
            return false; // Even numbers > 2 are not prime
        }
        
        // Check odd divisors up to √n
        // We only need to check up to √n because if n has a factor > √n,
        // it must also have a corresponding factor < √n
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                return false; // Found a divisor, so not prime
            }
        }
        
        return true; // No divisors found, so it's prime
    }

    /**
     * Sums and returns the total of a partial harmonic series. This series is the
     * sum of all terms 1/i, where i ranges from 1 to {@code n} (inclusive). Ex:
     *
     * <pre>
     * n = 3: sum = 1/1 + 1/2 + 1/3 = 1.8333333333333333
     * </pre>
     *
     * @param n an integer
     * @return sum of partial harmonic series from 1 to {@code n}
     */
    public static double sumPartialHarmonic(final int n) {
        double sum = 0.0;
        
        // Sum the series: 1/1 + 1/2 + 1/3 + ... + 1/n
        for (int i = 1; i <= n; i++) {
            // Use 1.0/i to ensure floating-point division, not integer division
            sum += 1.0 / i;
        }
        
        return sum;
    }
}
