# Midterm W 25 solution

### Object-Oriented Programming (Wilfrid Laurier University)

```
Scan to open on Studocu
```
```
Studocu is not sponsored or endorsed by any college or university
```
# Midterm W 25 solution

### Object-Oriented Programming (Wilfrid Laurier University)

```
Scan to open on Studocu
```
```
Studocu is not sponsored or endorsed by any college or university
```

# Midterm Examination Cover Sheet

## Do not begin the examination or attempt to read the examination

## questions until instructed to do so.

```
You must sign into the exam and show your Laurier student identification card when
```
## requested.

```
Students are expected to write their examinations in an honest manner. Where there are
reasonable grounds for believing a violation of exam protocol has occurred, students will
be subject to the disciplinary procedures and sanctions according to the Senate Policy 12.2 :
Student Code of Conduct: Academic Misconduct.
No device that can connect to the internet or Bluetooth, or any content or materials of any
kind not explicitly approved by the instructor, can be carried, accessed, set on the desk, or
worn on the person.
Ensure your name and WLU ID is written on all materials.
If you require assistance, please raise your hand.
Students may enter the exam room quietly up to 30 minutes after the scheduled start, but
no extra time will be given for late arrivals. Students cannot leave the room for any reason
within the first 30 minutes of the exam. Students must remain seated and cannot leave
during the last 15 minutes of the exam.
Only clear bottled water is allowed in the examination room; no other food or drink is
permitted.
```
```
Full examination regulations can be found in the Academic Calendar.
```
Term: Winter 25

Course Code: CP

Course Title: Object Oriented Programming

Instructor(s): Dr. Zara Hamid

Number of Pages (including cover
sheet):

```
17
```
Length of Exam: 60 mins

Examination Aids Permitted:
No aids allowed


## Section A

1. When no constructor is defined in class what happens?

```
a. The class cannot be instantiated.
b. An error occurs
c. The class becomes a static class.
d. Java provides a default no-argument constructor.
```
2. What is the primary purpose of the ‘this’ keyword in Java?
    a. To refer to a method parameter.
    b. To create a new object of the class.
    c. To refer to the current instance of the class.
    d. None of the above
3. If there are one or more constructors for a class then
    a. Exactly one of the constructors will be called each time an object of that class is
       created
    b. All of the constructors will be called each time an object of that class is created
    c. A destructor must also be written.
    d. None of the above
4. What is the ternary operator equivalent to the below code snippet? isDiscount( ) method
    returns a boolean value.

```
int price;
if (this.isDiscount()) {
price = 20;
} else {
price = 50;
}
```
```
a. int price = (this.isDiscount()) : 20? 50 ;
b. int price = (this.isDiscount())? 20: 50 ;
c. int price = (this.isDiscount())? 50: 20 ;
d. int price = (this.isDiscount()) : 20: 50 ;
```

5. What will be the output of the following Java program?

```
class access
{
public int x;
static int y;
void cal(int a, int b) {
x += a ;
y += b; }
}
class static_specifier
{
public static void main(String args[])
{
access obj1 = new access();
access obj2 = new access();
obj1.x = 0;
obj1.y = 0;
obj1.cal(1, 2);
obj2.x = 0;
obj2.cal(2, 3);
System.out.println(obj1.x + " " + obj2.y);
}
}
a) 1 2
b) 2 3
c) 3 2
d) 1 5
```

6. What will be the output of the following Java code?

```
class output
{
public static void main(String args[])
{
String s1 = "Hello I love java";
String s2 = new String(s1);
System.out.println((s1 == s2) + " " + s1.equals(s2));
}
}
```
```
a. true true
b. false false
c. true false
d. false true
```
7. An array object, ArrayOne, is created as:
    float [][] ArrayOne;
    ArrayOne = new float[20][10];
    Suppose ArrayOne is passed as an argument to a method in which the corresponding
    parameter is
    named someArray. What should the declaration of someArray look like in the parameter
    list of
    the method?
    (a) float [][] someArray
    (b) float someArray[]
    (c) float [] someArray[20]
    (d) float someArray[20][10]
8. Which of the following statements are incorrect?


```
a. static methods can call other static methods only
b. static methods must only access static data
c. static methods can not refer to this or super in any way
d. when object of class is declared, each object contains its own copy of static variables
```
9. A variable whose meaning is confined to an object of a class is called:

```
a. instance variable
b. local variable
c. global variable
d. none of the above
```
10. How many bytes will be reserved in memory for an instance of the following class, assuming that
    each int variable is 8 bytes, double is 16 bytes and boolean is 1 byte.

```
public class Employee {
```
```
private static double NumberofEmployees=0.0;
private int age;
private double salary;
private boolean retired;
}
```
```
a. 41
b. 25
c. 33
d. 49
```

## Section B

[16 marks] This section contains 8 questions with each question worth 2 marks.

11. What will be the output of the following Java program?

```
String phrase = "Fall Break!";
String part = phrase.substring(2,7);
intA = phrase.length();
ch = phrase.charAt(1);
System.out.println(intA + " " + part + " " + ch);
```
12. public class MidExam {
    public static void main(String[] args) {
       String S1 = "Java Programming";
       String S2 = " is taught";
       String S3 = " at Colorado State";
       int iSize = S3.length() + 3;
       System.out.println(iSize);
       char cChar = S1.charAt(10);
       System.out.println(cChar);
       int iIndex = S2.indexOf("p");
       System.out.println(iIndex);
       String sSubstr = S1.substring(1, 7);
       System.out.println(sSubstr);
       boolean bEquals = S2.equals(" is taught");


```
System.out.println(bEquals);
}
```
}

```
20
A
```
- 1
ava Pr
True
13. What will be the output of the following Java program?

```
String s = "midterm time";
intA = 11;
while ( intA > 0 ) {
switch (s.charAt(intA)) {
case 'd': case ' ': System.out.print(" a "); break;
case 'e': System.out.print(" b ");
case 't': System.out.print(" c "); break;
case 'r': System.out.print(" d ");
case 'm': System.out.print(" e "); break;
case 'I': case 'y':
default: System.out.print(" + ");
}
intA = intA - 2;
}
```

14. What would the following print?

```
int x = 3;
int y = 2;
if (y / x > 0)
System.out.print("first ");
System.out.print("second ");
```
```
second
```
15. Write out the output of the following code in the spaces provided.
    public class MidExam
       {
       public static void main(String[] args) {
       // Declare and allocate array
       double array[] = new double[5];
       // Initialize array
       for (int index = 0; index < array.length; index++)
       array[index] = (index * 3.0) + 0.5;
       // Print array information
       System.out.printf(“%.2f%n”, array.length-2);
    System.out.printf(“%.2f%n”, array[2]);
    System.out.printf(“%.2f%n”,array[3]* 2.0);
    System.out.printf(“%.2f%n”, array[4]+0.45);
    System.out.printf(“%.2f%n”, array[5]));
    }
    }


```
First line of output: 3
Second line of output: 6.
Third line of output: 19.
Fourth line of output: 12.
Fifth line of output: Exception (Out of bounds)
```
16. Write a declaration for an array variable people that could be used to refer to an array of
    Person objects and write a statement to create such array.

```
Person [] people;
People = new Person[10]
```
17. What might go wrong with the following code, what would you need to do to fix it. [
    marks]
       public class Test
       { int x;
       int y;
       public Test (int x, int y)
       { x = x;
       y = y;
       }
       }


```
The compiler may not be able to differentiate between local variable x and instance variable
x. Recommended to use this keyword with instance variable.
```
```
this.x=x;
this.y=y;
```
18. Given the following code and a file named “data.txt” whose contents are listed on the next
    page, show what is printed. Assume that all required imports are defined above the code
    shown. If an exception occurs, write the word exception for that output line.
       public class MidExam {
       public static void main(String[] args) {
       int i0 = 2, i1 = 3;
       double d0 = 2.0, d1 = 3.0, d2 = 4.0;
       char c0 = '8', c1 = 'Z';
       String s0 = "", s1 = "";
       try {
       Scanner scan = new Scanner(new File(“data.txt”));
       d0 = scan.nextDouble();
       i0 = scan.nextInt();
       c0 = scan.next().charAt(3);
       s0 = scan.next();
       System.out.println(d0 + ": " + i0);
       System.out.println(c0 + ": " + s0);
       if (scan.hasNextDouble())
       d1 = scan.nextDouble();
       if (scan.hasNextInt())
       i1 = scan.nextInt();
       c1 = scan.next().charAt(3);
       scan.nextLine(); // discard newline


```
s1 = scan.nextLine();
System.out.println(d1 + ", " + i1);
System.out.println(c1 + ", " + s1);
d2 = scan.nextDouble();
System.out.println(d2);
scan.close();
} catch (Exception e) {
System.out.println("Exception!");
}
}
}
```
Here are the contents of the file named “data.txt”:

Line 0: 57.31 22

Line 1: Computer Science

Line 2: 332211 1234.

Line 3: Have a nice summer!

Line 4: 468.

```
First line of output: 57.31: 22
Second line of output: p: Science
Third line of output: 332211.0, 3
Fourth line of output: 4, Have a nice summer!
Fifth line of output: 468.
```

## Section C

19. [6 marks] Write a complete Java program that prompts the user to enter an integer. If the
    number is a multiple of 5, print HiFive. If the number is divisible by 2 or 3, print Waterloo,
    otherwise do not print anything. If the user enters 1, end the program.
    Here are the sample runs:

```
Enter an integer: 6
Waterloo
Enter an integer: 15
HiFive Waterloo
Enter an integer: 25
HiFive
Enter an integer: 17
Enter an integer: 1
```
```
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
```
```
while (true) {
System.out.print("Enter an integer (enter 1 to exit): ");
int number = scanner.nextInt();
```
```
if (number == 1) {
System.out.println("Exiting program...");
break;
}
```
```
boolean printed = false;
if (number % 5 == 0) {
System.out.println("HiFive");
printed = true;
}
if (number % 2 == 0 || number % 3 == 0) {
System.out.println("Waterloo");
printed = true;
}
}
scanner.close();
}
```

20. ( 16 marks) Consider the following class definition that is written without methods. Instead, it
    has comments followed by blank areas denoted by empty box to describe what each
    method has to do. Add method definitions in those blank areas as indicated in the
    comment.

```
/**
* The VideoTape class holds information about a single television programme recorded on a
* video tape and it is used in a video shop system. It holds the video tape details.
*/
public class VideoTape
{
private String title; // the title of the programme
private String classification; // classification of the programme (comedy, drama,
action, or romance)
private int time; // the running time of the programme in minutes
```
// Create a new video tape with a given title, classification, and time. (2 marks)

```
public VideoTape (String title, String classification, int time )
{ this.title = title;
this.classification = classification;
this.time = time;
}
// Create a copy construct for the video tape class. ( 3 marks)
public VideoTape (VideoTape Other)
{ this.title = other.title;
this.classification = other.classification;
this.time = other.time;
}
```

```
// Return the title of this video tape. (2 marks)
public String getTitle() {
return this.title // return title is also correct
}
// Return the classification of this video tape. (2 marks)
public String getClassification() {
return this.classification // return classification is also correct
}
// Return the time of this video tape as a string in the following format: 2:06. (2 marks)
public String getTime() {
return this.time // return time is also correct
}
// Set a new classification for this video tape. (2 marks)
```
public void setClassification(String s) {

this.classification=new String(s); // this.classification=s is also correct

}

/* Define toString() method to print the details of the video tape to the output terminal in the
following format: ( 3 marks)

* Adil Emam (COMEDY) 2 0

*/

public String toString()

{

String s = “this.title” + “ ” + “(“ + “this.classification” + “)” + “ “ +”this.time”;

return s

}


