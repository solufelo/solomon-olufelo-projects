package cp213;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.awt.print.PrinterException;
import java.awt.print.PrinterJob;
import java.text.DecimalFormat;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

/**
 * The GUI for the Order class.
 *
 * @author Solomon Olufelo, 210729170, oluf9170@mylaurier.ca
 * @author Abdul-Rahman Mawlood-Yunis
 * @author David Brown
 * @version 2025-09-07
 */
@SuppressWarnings("serial")
public class OrderPanel extends JPanel {

    /**
     * Implements an ActionListener for the 'Print' button. Prints the current
     * contents of the Order to a system printer or PDF.
     */
    private class PrintListener implements ActionListener {

	@Override
	public void actionPerformed(final ActionEvent e) {
	    PrinterJob job = PrinterJob.getPrinterJob();
	    job.setPrintable(order);
	    if (job.printDialog()) {
		try {
		    job.print();
		} catch (PrinterException ex) {
		    ex.printStackTrace();
		}
	    }
	}
    }

    /**
     * Implements a FocusListener on a JTextField. Accepts only positive integers,
     * all other values are reset to 0. Adds a new MenuItem to the Order with the
     * new quantity, updates an existing MenuItem in the Order with the new
     * quantity, or removes the MenuItem from the Order if the resulting quantity is
     * 0.
     */
    private class QuantityListener implements FocusListener {
	private MenuItem item = null;
	private JTextField field = null;

	QuantityListener(final MenuItem item, final JTextField field) {
	    this.item = item;
	    this.field = field;
	}

	@Override
	public void focusGained(final FocusEvent e) {
	    // Do nothing when focus is gained
	}

	@Override
	public void focusLost(final FocusEvent e) {
	    String text = field.getText().trim();
	    int quantity = 0;
	    
	    try {
		quantity = Integer.parseInt(text);
		if (quantity < 0) {
		    quantity = 0;
		}
	    } catch (NumberFormatException ex) {
		quantity = 0;
	    }
	    
	    field.setText(String.valueOf(quantity));
	    order.update(item, quantity);
	    updateTotals();
	}
    }

    // Attributes
    private Menu menu = null;
    private final Order order = new Order();
    private final DecimalFormat priceFormat = new DecimalFormat("$##0.00");
    private final JButton printButton = new JButton("Print");
    private final JLabel subtotalLabel = new JLabel("0");
    private final JLabel taxLabel = new JLabel("0");
    private final JLabel totalLabel = new JLabel("0");

    private JLabel nameLabels[] = null;
    private JLabel priceLabels[] = null;
    // TextFields for menu item quantities.
    private JTextField quantityFields[] = null;

    /**
     * Displays the menu in a GUI.
     *
     * @param menu The menu to display.
     */
    public OrderPanel(final Menu menu) {
	this.menu = menu;
	this.nameLabels = new JLabel[this.menu.size()];
	this.priceLabels = new JLabel[this.menu.size()];
	this.quantityFields = new JTextField[this.menu.size()];
	this.layoutView();
	this.registerListeners();
    }

    /**
     * Uses the GridLayout to place the labels and buttons.
     */
    private void layoutView() {
	// Grid: rows = menu items + header + subtotal + tax + total + print button
	// columns = 3 (Item, Price, Quantity)
	int rows = this.menu.size() + 5;
	this.setLayout(new GridLayout(rows, 3));
	
	// Header row
	this.add(new JLabel("Item"));
	this.add(new JLabel("Price"));
	this.add(new JLabel("Quantity"));
	
	// Menu items rows
	for (int i = 0; i < this.menu.size(); i++) {
	    MenuItem item = this.menu.getItem(i);
	    
	    // Create and store labels
	    this.nameLabels[i] = new JLabel(item.getName());
	    this.priceLabels[i] = new JLabel(this.priceFormat.format(item.getTariff().doubleValue()));
	    
	    // Create and store text field
	    this.quantityFields[i] = new JTextField("0");
	    
	    // Add to layout
	    this.add(this.nameLabels[i]);
	    this.add(this.priceLabels[i]);
	    this.add(this.quantityFields[i]);
	}
	
	// Subtotal row
	this.add(new JLabel("Subtotal:"));
	this.add(this.subtotalLabel);
	this.add(new JLabel(""));
	
	// Tax row
	this.add(new JLabel("Taxes:"));
	this.add(this.taxLabel);
	this.add(new JLabel(""));
	
	// Total row
	this.add(new JLabel("Total:"));
	this.add(this.totalLabel);
	this.add(new JLabel(""));
	
	// Print button row
	this.add(this.printButton);
	this.add(new JLabel(""));
	this.add(new JLabel(""));
	
	// Initialize totals
	this.updateTotals();
    }
    
    /**
     * Updates the subtotal, tax, and total labels.
     */
    private void updateTotals() {
	this.subtotalLabel.setText(this.priceFormat.format(this.order.getSubTotal().doubleValue()));
	this.taxLabel.setText(this.priceFormat.format(this.order.getTaxes().doubleValue()));
	this.totalLabel.setText(this.priceFormat.format(this.order.getTotal().doubleValue()));
    }

    /**
     * Register the widget listeners with the widgets.
     */
    private void registerListeners() {
	// Register the PrinterListener with the print button.
	this.printButton.addActionListener(new PrintListener());

	// Register QuantityListener for each quantity field
	for (int i = 0; i < this.menu.size(); i++) {
	    MenuItem item = this.menu.getItem(i);
	    this.quantityFields[i].addFocusListener(new QuantityListener(item, this.quantityFields[i]));
	}
    }
}