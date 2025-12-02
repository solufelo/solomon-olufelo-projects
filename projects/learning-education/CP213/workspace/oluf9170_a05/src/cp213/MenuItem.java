package cp213;

import java.math.BigDecimal;

/**
 * Defines the name and tariff of a menu item. tariff is stored as a BigDecimal
 * to avoid rounding errors.
 *
 * @author Solomon Olufelo, 210729170, oluf9170@mylaurier.ca
 * @author Abdul-Rahman Mawlood-Yunis
 * @author David Brown
 * @version 2025-09-07
 */
public class MenuItem {

    // Attributes
    private static final String itemFormat = "%-12s $%5.2f";
    private String name = null;
    private BigDecimal tariff = null;

    /**
     * Constructor. Must set tariff to 2 decimal points for calculations.
     *
     * @param name   name of the menu item.
     * @param tariff cost of the menu item.
     */
    public MenuItem(final String name, final BigDecimal tariff) {
	this.name = name;
	this.tariff = tariff.setScale(2, java.math.RoundingMode.HALF_UP);
    }

    /**
     * Alternate constructor. Converts a double tariff to BigDecimal.
     *
     * @param name   name of the menu item.
     * @param tariff cost of the menu item.
     */
    public MenuItem(final String name, final double tariff) {
	this.name = name;
	this.tariff = BigDecimal.valueOf(tariff).setScale(2, java.math.RoundingMode.HALF_UP);
    }

    /**
     * name getter
     *
     * @return name of the menu item.
     */
    public String getName() {
	return this.name;
    }

    /**
     * tariff getter
     *
     * @return cost of the menu item.
     */
    public BigDecimal getTariff() {
	return this.tariff;
    }

    /**
     * Returns a MenuItem as a String in the format:
     *
     * <pre>
    hot dog      $ 1.25
    pizza        $10.00
     * </pre>
     */
    @Override
    public String toString() {
	return String.format(itemFormat, this.name, this.tariff.doubleValue());
    }
}