package cp213;

import java.time.LocalDate;

/**
 * Tests the Student class.
 *
 * @author your name here
 * @version 2022-01-17
 */
public class Main {

    public static void main(String[] args) {
	final String line = "-".repeat(40);
	int id = 123456;
	String surname = "Brown";
	String forename = "David";
	LocalDate birthDate =  LocalDate.parse("1962-10-25");
	Student student = new Student(id, surname, forename, birthDate);
	System.out.println("New Student:");
	System.out.println(student);
	System.out.println(line);
	System.out.println("Test Getters");

	// Test all getter methods
	System.out.println("ID: " + student.getId());
	System.out.println("Surname: " + student.getSurname());
	System.out.println("Forename: " + student.getForename());
	System.out.println("Birth Date: " + student.getBirthDate());

	System.out.println(line);
	System.out.println("Test Setters");

	// Test all setter methods
	student.setId(654321);
	student.setSurname("Smith");
	student.setForename("John");
	student.setBirthDate(LocalDate.parse("1995-05-15"));

	System.out.println("Updated Student:");
	System.out.println(student);
	System.out.println(line);
	System.out.println("Test compareTo");

	// Create new Students and test comparisons
	Student student1 = new Student(111111, "Anderson", "Alice", LocalDate.parse("1990-03-20"));
	Student student2 = new Student(222222, "Brown", "Bob", LocalDate.parse("1992-07-10"));
	Student student3 = new Student(333333, "Brown", "Charlie", LocalDate.parse("1991-12-05"));
	
	// Test compareTo method
	System.out.println("Comparing " + student1.getSurname() + " with " + student2.getSurname() + 
			   ": " + student1.compareTo(student2));
	System.out.println("Comparing " + student2.getSurname() + " with " + student3.getSurname() + 
			   ": " + student2.compareTo(student3));
	System.out.println("Comparing " + student3.getSurname() + " with " + student2.getSurname() + 
			   ": " + student3.compareTo(student2));
    }

}
