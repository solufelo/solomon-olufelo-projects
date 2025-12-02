package cp213;

import java.time.LocalDate;

/**
 * Student class definition.
 *
 * @author your name here
 * @version 2022-01-17
 */
public class Student implements Comparable<Student> {

    // Attributes
    private LocalDate birthDate = null;
    private String forename = "";
    private int id = 0;
    private String surname = "";

    /**
     * Instantiates a Student object.
     *
     * @param id        student ID number
     * @param surname   student surname
     * @param forename  name of forename
     * @param birthDate birthDate in 'YYYY-MM-DD' format
     */
    public Student(int id, String surname, String forename, LocalDate birthDate) {
	// Assign attributes to instance variables
	this.id = id;
	this.surname = surname;
	this.forename = forename;
	this.birthDate = birthDate;

	return;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#toString() Creates a formatted string of student data.
     */
    @Override
    public String toString() {
	// Create formatted string with all student information
	String string = String.format("Student [ID: %d, Surname: %s, Forename: %s, Birth Date: %s]", 
				      this.id, this.surname, this.forename, this.birthDate);

	return string;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Comparable#compareTo(java.lang.Object)
     */
    @Override
    public int compareTo(final Student target) {
	int result = 0;

	// Compare students by surname first, then by forename if surnames are equal
	result = this.surname.compareTo(target.surname);
	if (result == 0) {
	    result = this.forename.compareTo(target.forename);
	}

	return result;
    }


    // getters and setters defined here
    
    /**
     * Gets the student's birth date.
     * @return the birthDate
     */
    public LocalDate getBirthDate() {
	return this.birthDate;
    }

    /**
     * Gets the student's forename.
     * @return the forename
     */
    public String getForename() {
	return this.forename;
    }

    /**
     * Gets the student's ID.
     * @return the id
     */
    public int getId() {
	return this.id;
    }

    /**
     * Gets the student's surname.
     * @return the surname
     */
    public String getSurname() {
	return this.surname;
    }

    /**
     * Sets the student's birth date.
     * @param birthDate the birthDate to set
     */
    public void setBirthDate(LocalDate birthDate) {
	this.birthDate = birthDate;
    }

    /**
     * Sets the student's forename.
     * @param forename the forename to set
     */
    public void setForename(String forename) {
	this.forename = forename;
    }

    /**
     * Sets the student's ID.
     * @param id the id to set
     */
    public void setId(int id) {
	this.id = id;
    }

    /**
     * Sets the student's surname.
     * @param surname the surname to set
     */
    public void setSurname(String surname) {
	this.surname = surname;
    }

}
