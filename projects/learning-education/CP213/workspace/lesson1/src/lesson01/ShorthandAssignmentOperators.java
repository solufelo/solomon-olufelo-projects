package lesson01;

public class ShorthandAssignmentOperators {
	static int count = 0, sum = 0, bonus = 2, time = 360, rushFactor = 10, change = 37, discount = 5, count1 = 5,
			count2 = 12, amount = 4;

	public static void print() {
		System.out.println(
				"variable values are " + count + " " + sum + " " + time + " " + bonus + " " + change + " " + amount);
	}

	public static void main(String args[]) {
		count += 2;
		sum -= discount;
		bonus *= 2;
		time /= rushFactor;
		change %= 100;
		amount *= count1 + count2;
		System.out.println("Shorthand operators are used");
		print();

		System.out.println("-----------------------");
		System.out.println("Variables are re-initalized");
		count = 0;
		sum = 0;
		bonus = 2;
		time = 360;
		rushFactor = 10;
		change = 37;
		discount = 5;
		count1 = 5;
		count2 = 12;
		amount = 4;

		count = count + 2;
		sum = sum - discount;
		bonus = bonus * 2;
		time = time / rushFactor;
		change = change % 100;
		amount = amount * (count1 + count2);
		System.out.println("Full expressions are used and the results are identical");
		print();
	}
}
