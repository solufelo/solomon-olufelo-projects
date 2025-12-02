# CP213 Final EXAM

## Object-Oriented Programming (Wilfrid Laurier University)

```
Scan to open on Studocu
```
```
Studocu is not sponsored or endorsed by any college or university
```
# CP213 Final EXAM

## Object-Oriented Programming (Wilfrid Laurier University)

```
Scan to open on Studocu
```
```
Studocu is not sponsored or endorsed by any college or university
```

## 213 FINAL EXAM REVIEW

### Protected access: child classes to this class canaccess the method/variables even if

_they aren't in the same package_

_**There are 2 classifications of instance variables& methods that allow them to be accessed
by name in aderived class** →one of them is protectedaccess (always gives access)_

```
➔ If a method/instance variable is modified by protected (rather than
public/private) → itcan be accessed by name insideits own classdefinition
◆ it can be accessed by name inside any class derivedfrom it
◆ it can also be accessed by name in the definition of anyclass in the
same package(even if the class in the same packageis not derived
from it)
◆ Can be accessed in a different package if the classis derived from it
```
```
★ Example: consider theclass HourlyEmployeethat wasderived from the baseclass
Employee.
```
```
If the private instance variables name & hireDate had been marked protected in the
class Employee, the definition of toString in thederivedclass HourlyEmployeecould
be simplified to the following:(basically removedthe “get”)
```
#### Pitfall: A Restriction on Protected Access ★

```
● A class can access its own classes’ inherited variables & methods that are marked
protected in the base class, but cannot directly access any such instance variables
● For example, n is an instance variable of the base class B & an instance variable of the
derived class D. D can access n whenever n is used as an instance variable of D, but D
cannot access n when n is used as an instance variable of B.
```

```
● If the classes B and D are in the same package, you will not get the error message
because, in Java, protected access implies package access.
```
### Package/Friendly/Default access: each class that isderived from the same

_package has access to this method/variables_

_**There are 2 classifications of instance variables& methods that allow them to be accessed
by name in aderived class** →one of them is packageaccess(gives access if the derived class
is in the same package as the base class)_

```
● If you do not place any of these modifiers (public, private, or protected) before
an instance variable or method definition → then the instance variable/method
can be accessed by name inside the definition of any class in thesame
packagebut not outside of the package → package access
○ Use package access in situations → package of cooperating classes that
act as a single encapsulated unit
○ Package access is more restricted than protected
○ Package access givesmore control to the programmerdefining the
classes
○ If you control the package directory (folder) → you control who is allowed
package access
```
#### Pitfall: Forgetting about the default package ★

```
● If a class in your current directory is not in any other package→ then it is in
the default package
● If an instance variable/method has package access → then it can be accessed
by name in the definition of any other class in the default package
```
### Public access: Any class can access this regardlessof package or whatever

```
➔ The public access modifier is thedirect oppositeof the private access
modifier
◆ A class, method or variable can be declared as public → is accessible
from any class
◆ It can be accessed in its own class
◆ Can be accessed from a different class
◆ Can be accessed from a different package
```

### Private access: Means that only members of this class have access to this method/

_variable_

```
➔ The most restricted access level
◆ Can only be accessed in its own class & same package
```
```
➔ Class & interfaces cannot be private
➔ Variables that are declared private can be accessed outside the class → if
public getter methods are present in the class
```
```
★ ALL 4 ACCESS (private, public, package, protected)
```

### Final Modifier: methods cannot be overridden by other classes, prevents inheritance

```
➔ If themodifier finalis placed before the definitionof a method → thatmethod
may not be redefined/overriddenin a derived class
```
```
➔ If themodifier finalis placed before the definitionof a class → thatclass may
not be used as a base class to deriveother classes(prevents inheritance)
```
```
➔ If themodifier finalis placed before a variable→thatvariable cannot be
changed because it has a constant value
```
```
● If a method is marked as final → the compiler canuse early binding with that
particular method (enables the compiler to be more efficient)
○ the added efficiency is normally not great & suggestedto not use the
final modifier solely for reasons of efficiency (itcan sometimes aid security to
mark certain methods as final)
```
```
● You can view the final modifier as a way of turningoff late binding for a
method (or an entire class)
```

### Instance Variables: defined in a class, each instance of the class has a separate

_copy of the variable_

```
➔ Instance variables → non-static variables which are defined in a class outside
any method,constructoror a block
```
#### ◆ Each instance of the class has a separate copy ofthe variable

#### ◆ instance variable belongs to a class

#### ◆ When you create a new object of the class you createan instance

```
➔ Features:
```
#### ◆ Every object will have its own copy of Instance variables

#### ◆ Initializationof instance variables is not compulsory→default value is 0

#### ◆ Access modifiers can be assigned to instance variables

### Static Variables: belongs to a whole class not just 1 object, only one copy of the

_variable_

```
➔ Static variables → variable that belongs to the classas a whole & not just to
one object
```
#### ◆ there is only one copy of the variable & all the objectscan use this one

```
variable
```
#### ◆ can be used by objects to communicate between theobjects (One

```
object can change the static variable & another object can read that change)
```
#### ◆ To make a variable static → declare it like an instancevariable but add

```
the modifier static →private staticintturn;
➔ Features:
```
#### ◆ Initialization of static variables is not compulsory →default boolean

```
value is False
◆ Staticvariablesofother primitivetypes → automaticallyinitializedto
the zero of their type
◆ Staticvariablesofaclasstype→ automaticallyinitializedtonull (which
is a kind of placeholder for an object)
◆ Static variables in a base class are inherited byany of its derived classes
◆ Staticvariablesshouldnormallybeprivate,unlesstheyhappentobe
defined constants(would be marked final)
```

### Abstract class: restricted class that cannot be used to create objects → It must

be inherited from (uses the " **abstract** " keyword)

```
➔ In order to postpone the definition of a method →abstract methodto be
declared
◆ An abstract method has a heading, but no method body
◆ The body of the method is defined in the derived classes
```
```
◆ The class that contains an abstract method ( 1 or many) → abstract class
◆ Abstract method → placeholder for a method that willbe fully defined
in a descendent class
● It has a complete method heading(which has been addedthe modifier abstract)
● It cannot be private
● It ends with a semicolon in place of its body
○ public abstract double getPay();
○ public abstract void doIt(int count);
```
```
➔ Abstract class must have the modifier abstract includedin its class heading :
public abstract class Employee
{
private instanceVariables;
public abstract double getPay();
...
}
```
**Pitfall: You Cannot Create Instances of an Abstract Class**

```
● Abstract class can only be used to derive more specializedclasses
○ Example: While it may be useful to discuss employees in general, in reality an
employee must be a salaried worker or an hourly worker
● Abstract class constructor cannot be used to createan object of the abstract
class
○ However, a derived class constructor will include an invocation of the
abstract class constructor in the form of super
```
**Tip: An Abstract Class Is a Type**

```
● It is perfectly fine to have a parameter of an abstractclass type (this makes it
possible to plug in an object of any of its descendent classes)
```
```
● It is also fine to use a variable of an abstract classtype → as long is it names
objects of its concrete descendent classes only
```

### Concrete class: a class with no abstract methods

```
➔ Concrete method: the method has complete definition but it can be
overridden in the inherited class
```
### Generics class: a generic type is a generic class/interfacethat is parameterized over

_types_

```
➔ Generic programming with a type parameter allows youto write code that
applies to any class(usually a single uppercase letter(T) is used as a type parameter)
```
```
➔ Code that uses generics have many benefits over non-genericcode
```
```
➔ Generic Interfaces → can have one or more type parameters
```
```
◆ Stronger type checks at compile time(issues errorsif the code violates
type safety)
● Fixing compile-time errors is easier than fixing runtimeerrors,
which can be difficult to find
◆ Elimination of casting/casts
```
```
◆ By using generics→ Generic algorithms can implemented that can
work on collections of different types
● Can be customized & Easier/safer to read
● Class type plugged in type parameter must be specified →
“instantiate” the generic class
```
```
➔ Type Parameter : angular brackets, defined in a generic/parameterizedclass
```
**Pitfall: A Generic Constructor name has no type parameter**

```
● Type parameter is not used in the heading of the constructordefinition
```
```
○ Can be used as a type for the parameter → no angularbrackets
```
```
○ When generic class is instantiated → angular bracketsare used
```
**Pitfall: A primitive type cannot be plugged in for a type parameter**

```
● Type plugged in for type parameter must always be a reference not (int, string)
```
**Pitfall: A Type Parameter Cannot Be Used Everywhere a Type Name Can Be Used**


**Pitfall: An Instantiation of a Generic Class Cannot be an Array Base Type**

**Pitfall: A Class Definition Can Have More Than One Type Parameter**

```
● Separated by commas
```
**Pitfall: AGeneric Class Cannot Be an Exception Class**

```
● It cannot have throwable objects, exceptions, error → will generate a compile
error
```
### GUI

```
● GUI (graphical user interface)→ is a windowing systemthat interacts with the
user
○ Swing GUIs are designed using →event-driven programming(OOP)
○ Creating GUIs →Java AWT(Abstract Window Toolkit)
○ GUI component → object that fires an event
○ Infinite loops → GUI programs are like that, so mustuseSystem.exit
○ GUI Built using Swing container→ 3 objects (container,components,
layout manager)
```
### JPanel → stores groups of components, combines smallerobjects to larger component

```
● GUI → is often organized in a hierarchical fashion ,with containers called
panels inside other containers
● Panel → an object of the JPanel class that servesas a simple container
```
```
○ Main functions of a JPanel object → subdivide a JFrameor other
container
○ The classes JFrame & JPanel are descendent classesof the class
Container
```
```
○ Place the text field(s) & label(s) in a JPanel
○ Treat the JPanel as a single component
○ A JPanel is a JComponent but a JFrame is a Componentnot a
JComponent
○ JPanel object is analogous to the braces used to combinea number of
simpler Java statements into a single larger Java statement
```

### JMenu In swing's GUI package it's an implementation of a menu in a popup window

_that is displayed when the user selects an item on the JMenuBar_

```
● Menu is an object of the class → JMenu
○ A choice on a menu is called a menu item & is an object of the class
JMenuItem
● Class JMenu →descendent of the JMenuItem class
```
```
● Every JMenu can be a menu item in another menu
```
```
● Amenu item is identified by the string that labelsit,such as "Blue", "White", or
"Gray" in the menu
```
```
● You can add as many JMenuItems as you wish to a menu
○ The menu lists the items in the order
```
### JTextArea

```
● Text area is an object of the class → JTextArea
○ Text area → same as a text field except that it allowsmultiple lines
○ Two parameters → the min # of lines & the min # ofcharacters per line
that are guaranteed to be visible
```
```
● You can enter any amount of text in a text area, but only a limited number of
lines & a limited number of characters per line willbe visible
○ For example → the following creates a JTextArea named theText that
will have at least 5 lines & at least 20 characters per line visible
```

# Inheritance

```
● Inheritance is the process by which a new class is created from another class
○ The new class is called the derived class while the original is the base class
○ Inheritance helps with code reusability
○ Derived class has all instance variables and methods of base class and may
contain additional instance variables and methods
```
##### ○

```
● Superclass/parent class/base class: the class being inherited from
○ The parent of a parent class is called an ancestor class
○ If A is an ancestor of B, then B is a descendent of A
● Subclass/child class/derived class: the class that inherits from another class
● Subclass inherits the superclass’ attributes (instance variables) and methods
○ Can add more specialization
● When u create subclass: add “extends SuperClassName ”when declaring the class
● Method overriding is when a child class uses a parent class’s method without changing
the parameters or return type. Only the method definition is changed
```
##### ○


##### ●

○ Method overloading is early binding while method overriding is late binding
○ Method overloading in java is a feature that allows a class to have more than one
method with the same name, but with different parameters.
● Upcasting: Upcasting is thetypecastingof a childobject to a parent object. Upcasting
can be done implicitly
● Downcasting: Similarly, downcasting means the typecasting of a parent object to a child
object. Downcasting cannot be implicit.

##### ●


# Exception (try-throw-catch Mechanism)

```
● Try- the try block of code tells us what to do when everything goes smoothly. It tries to
execute a case in which everything goes without error.
● Catch- A throw statement calls a catch block whichbegins execution after execution of
the try block is stopped.
○ Handling the exception - Handling the exception refers to the execution of the
catch block which is executed whenever an exception is thrown and handles the
exception.
○ Catch block parameter- the catch block has one parameterwhich is the
exception object thrown.
```
##### ■

##### ●

```
● Throw and throws operator
○ Throw - The value thrown (which is the argument of the throw operator) is always
an object of some exception class. After throwing an exception, the execution of
the try block is stopped and the catch block is executed.
■ The execution of a throw statement is called throwingan exception
■ A throw statement calls the catch block
■ throw new ExceptionClassName(SomeString);
```
##### ■


##### ○

```
● The base program is placed in thetryblock, errorand exception handling
is placed in thecatchblock, and finishing up codeto be runwhether
exceptions take place or notis placed in thefinallyblock.
○ If an exception is thrown in the try block and there is no matching catch block in
the method, the finally block is executed.
● AnArrayIndexOutOfBoundsExceptionis thrown whenevera program attempts to use an
array index that is out of bounds
○ This normally causes the program to end
● TheNumberFormatExceptionis an unchecked exceptionin Java that occurs whenan
attempt is made to convert a string with an incorrect format to a numeric value.
Therefore, this exception is thrown when it is not possible to convert a string to a
numeric type (e.g. int, float).
```
# Polymorphism

##### ●

```
● Polymorphism vs Inheritance
```

##### ○

○ Polymorphism allowschanges to be made to method definitionsin the derived
classes, and have those changesapply to the softwarewritten for the base class
○ Polymorphism is the ability to associate multiple meanings to a single method
name through late binding or dynamic binding
■ Is a way to have the same method name do different things
○ Inheritance allows you to define a base class and to define software for the base
class. That software can then be used not only for objects of the base class but
also for objects of any class derived from the base class. Polymorphism allows
you to make changes in the method definition for the derived classes and to have
those changes apply to the software written in the base class.
● Bindingis the process of associating a method definitionwith a method call
● Early binding or static binding- If a method definitionis associated with a method call at
compile time, the process is called early binding or static binding
○ Static, final, and private methods are early bindingbecause they cannot be
overridden.


##### ○

■ Superclass B is an example of upcasting
● Early Binding
○ When the compiler determines the type of an object and resolves its method
during compile-time.
○ Heavily related to static binding
● Static Binding
○ Binding that is done on all static, private, and final methods
○ Heavily related to early binding
● Late binding or dynamic binding- If a method definitionis associated with a method call
at run time, the process is called late binding or dynamic binding
○ In the late binding or dynamic binding, the compiler doesn’t decide the method to
be called. Overriding is a perfect example of dynamic binding. In overriding both
parent and child classes have the same method.


##### ○

##### ●


# Interface

```
● Interface
○ An "abstract class" that is used to group related methods together using empty
bodies.
○ An interface is like an extreme case of an abstract class but it is not actually a
class but it is a type.
○ An interface is a type. This allows you to write a method with a parameter of an
interface type, such as a parameter of type Ordered, and that parameter will
accept as an argument any class you later define that implements the interface.
```
##### ○

```
● Derive an interface from a base interface
○ An interface (interface A) can implement another interface (interface B) by using
the "extends" keyword in its initial definition.
■ Ex: interface A extends B {
```
##### ○

```
● Implementing an interface
○ An interface specifies a set of methods that any class that implements the
interface must have
■ It containsmethod headings and constant definitionsonly
■ It containsno instance variables nor any completemethod definitions
```

■ An interface and all of its method headings should bedeclared public
■ When a class implements an interface, it must make all of the methods in
the interface public
○ A child class implements an interface as a parent class by using the
"implements" keyword.
○ Ex: class TestClass implements ParentInterface {
■ Multiple interfaces should be separated by a comma
● Concrete class implementing an interface
○ Must use _implements interfaceName_ keyword
○ The class mustimplement all the method headings(unlikein an abstract class)
listed in the definitions of the interfaces.

##### ○

● Abstract class implementing an interface
○ As you saw in the previous subsection, a concrete class (that is, a regular class)
must give definitions for all the method headings given in an interface in order to
implement the interface. However, you can define an abstract class that
implements an interface but givesonly definitionsfor some of the method


```
headings given in the interface. The method headings given in the interface that
are not given definitions aremade into abstract methods.
```
##### ○

● Comparable interface- The comparable interface isan interface that is part of the
java.lang package and is therefore available to any program. It is used to compare an
object of a class with an instance of that class.

##### ○

● Serializable interface- The serializable interfaceis part of the java.io package. It is a
marker interface meaning it does not have any methods and fields. Therefore, any class
that implements it does not need to implement any methods.
○ It is used merely as a type tag that indicates to the system that it may implement
file I/O in a particular way
● Cloneable Interface- The cloneable interface is alsoa marker interface and does not
have any method headings or defined constants. It is used to indicate how the clone
method which is inherited from the object class should be used and redefined.
○ The method Object.clone() does a bit-by-bit copy of the object's data in storage


# Inner and outer classes

```
● Inner classesare classes that are defined withinother classes. The class including the
inner class is called theouter class. Inner classesgroup classes that belong together.
Inner and outer classeshave access to each othersprivate methods.
```
##### ●

```
○ The inner class does not have to be private
● An inner class definition is amember of the outerclassin the same way that the
instance variables of the outer class and the methods of the outer class are members of
the outer class. Thus, aninner class definition islocal to the outer class definition. So
you may reuse the name of the inner class for something else outside the definition of
the outer class.
● If an inner class is private, then it cannot be accessed by name from outside the
definition of the outer class
● There are two big advantages to inner classes. First, because they are defined within a
class, they can be used to make the outer class self-contained or more self-contained
than it would otherwise be. The second advantage is that the inner and outer classes’
methodshave access to each other’s private methodsand private instance variables.
● Inner classes can be used as helping classes
● To access the inner class, create an object of the outer class, and then create an object
of the inner class:
```

##### ●

# Event-driven programming

```
● Event-driven programming: A programming paradigm inwhich the flow of the program is
determined by events such as user actions, sensor outputs, or message passing from
other programs/threads
○ Event-driven programming is a programming style that uses a
signal-and-response approachto programming. Signalsto objects are things
called events
● The ActionListener: An interface in AWT (AbstractWindow Toolkit) that listens for action
events.
● actionEvent(): A semantic event in AWT that indicatesan action happened
● actionPerformed(): The method in the actionEvent()class that indicates the event id of
the action performed
● Events and listeners
○ Swing programs use events and event handlers.
○ Anevent is an object that acts as a signal to anotherobject known as a listener.
The sending of the event is called firing the event.
○ Theobject that fires the event is often a GUI component,such as a button. The
button fires the event in response to being clicked.
○ Thelistener object performs some action in responseto the event. For example,
the listener might place a message on the screen in response to a particular
button being clicked. A given component may have any number of listeners, from
zero to several listeners. Each listener might respond to a different kind of event,
or multiple listeners might respond to the same events.
```

● Anexception object is an event. Thethrowing of an exception is an example of firing an
event(in this case, firing the exception event).Thelistener is the catch blockthat
catches the event.
● Thesemethods that handle events are calledeventhandlers. You the programmer will
define (or redefine) these event-handler methods. The relationship between an
event-firing object, such as a button, and its event-handling listener is shown
diagrammatically in Display 17.1.

##### ●


