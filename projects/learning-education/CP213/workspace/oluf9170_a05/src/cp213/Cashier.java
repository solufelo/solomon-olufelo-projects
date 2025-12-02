package cp213;

import java.util.Scanner;

/**
 * Wraps around an Order object to ask for MenuItems and quantities.
 *
 * @author Solomon Olufelo, 210729170, oluf9170@mylaurier.ca
 * @author Abdul-Rahman Mawlood-Yunis
 * @author David Brown
 * @version 2025-09-07
 */
public class Cashier {

    private Menu menu = null;

    /**
     * Constructor.
     *
     * @param menu A Menu.
     */
    public Cashier(Menu menu) {
	this.menu = menu;
    }

    /**
     * Reads keyboard input. Returns a positive quantity, or 0 if the input is not a
     * valid positive integer.
     *
     * @param scan A keyboard Scanner.
     * @return
     */
    private int askForQuantity(Scanner scan) {
	int quantity = 0;
	System.out.print("How many do you want? ");

	try {
	    String line = scan.nextLine();
	    quantity = Integer.parseInt(line);
	} catch (NumberFormatException nfex) {
	    System.out.println("Not a valid number");
	}
	return quantity;
    }

    /**
     * Prints the menu.
     */
    private void printCommands() {
	System.out.println("\nMenu:");
	System.out.println(menu.toString());
	System.out.println("Press 0 when done.");
	System.out.println("Press any other key to see the menu again.\n");
    }

    /**
     * Asks for commands and quantities. Prints a receipt when all orders have been
     * placed.
     *
     * @return the completed Order.
     */
    public Order takeOrder() {
	System.out.println("Welcome to WLU Foodorama!");
	Order order = new Order();
	Scanner keyboard = new Scanner(System.in);
	
	this.printCommands();
	
	boolean done = false;
	while (!done) {
	    System.out.print("Command: ");
	    String command = keyboard.nextLine().trim();
	    
	    try {
		int commandNum = Integer.parseInt(command);
		
		if (commandNum == 0) {
		    done = true;
		} else if (commandNum >= 1 && commandNum <= this.menu.size()) {
		    MenuItem item = this.menu.getItem(commandNum - 1);
		    int quantity = this.askForQuantity(keyboard);
		    if (quantity > 0) {
			order.add(item, quantity);
		    }
		} else {
		    System.out.println("Not a valid number");
		    this.printCommands();
		}
	    } catch (NumberFormatException e) {
		System.out.println("Not a valid number");
		this.printCommands();
	    }
	}
	
	keyboard.close();
	System.out.println("----------------------------------------");
	System.out.println("Receipt");
	System.out.print(order.toString());
	
	return order;
    }
}