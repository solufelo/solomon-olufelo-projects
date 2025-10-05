package cp213;

/**
 * @author Solomon Olufelo - 210729170 - oluf9170@mylaurier.ca
 * @version 2025-09-28
 */
public class LeapYear {

    /**
     * Determines whether or not a year is a leap year.
     * <p>
     * A leap year is defined as: <blockquote>Every year that is exactly divisible
     * by four is a leap year, except for years that are exactly divisible by 100,
     * but these centurial years are leap years if they are exactly divisible by
     * 400. For example, the years 1700, 1800, and 1900 are not leap years, but the
     * years 1600 and 2000 are.
     * <p>
     * Thus 1996, 2000, and 2004 are leap years, but 1899, 1900, and 1901 are not
     * leap years.</blockquote>
     * <p>
     * (United States Naval Observatory)
     *
     * @param year the year to test ({@code int} greater than 0)
     * @return {@code true} if {@code year} is a leap year, {@code false} otherwise.
     */
    public static boolean isLeapYear(final int year) {
        // Implementation based on leap year rules:
        // 1. Divisible by 4 → leap year
        // 2. EXCEPT divisible by 100 → not leap year  
        // 3. EXCEPT divisible by 400 → leap year
        
        // Using compound boolean logic with proper precedence
        return (year % 4 == 0) && (year % 100 != 0 || year % 400 == 0);
    }

    /**
     * Determines the number of leap years that have occurred between two given years.
     * Does not include the start and end years in the count.
     *
     * @param start the start year (int)
     * @param end   the end year (int)
     * @return the number of leap years between start and end, exclusive
     */
    public static int leapYearsBetween(final int start, final int end) {
        int count = 0;
        
        // Loop through years between start and end (exclusive)
        for (int year = start + 1; year < end; year++) {
            if (isLeapYear(year)) {
                count++;
            }
        }
        
        return count;
    }

    /**
     * Determines which day of the year a given date represents.
     * January 1st is day 1, December 31st is day 365 (or 366 in leap years).
     *
     * @param year  the year (int)
     * @param month the month (1-12) (int)
     * @param day   the day of the month (int)
     * @return the day of the year (1-366)
     */
    public static int dayOfYear(final int year, final int month, final int day) {
        // Days in each month (index 0 = January)
        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        // Adjust February for leap years
        if (isLeapYear(year)) {
            daysInMonth[1] = 29;
        }
        
        // Sum days from all complete months before the given month
        int totalDays = day; // Start with the day within the current month
        
        for (int i = 0; i < month - 1; i++) {
            totalDays += daysInMonth[i];
        }
        
        return totalDays;
    }
}