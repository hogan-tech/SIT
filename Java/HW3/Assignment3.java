
/**
 * @author: Hogan Lin
 * @class: CS501 Intro to Java
 * @description: Implementation of a school hierarchy, shape abstraction with generics,
 * and an employee management system using interfaces.
 * @date: March 25, 2025
 **/

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * Assignment 3: Simplified Object-Oriented Programming
 *
 * This assignment tests your ability to write classes, implement
 * object-oriented principles,
 * create abstract classes and interfaces, and use basic generics.
 */
public class Assignment3 {

    /**
     * Problem 1: School Hierarchy
     *
     * Design a school hierarchy with the following classes:
     * - `Person`: A superclass for `Student` and `Professor`.
     * - `Student`: Represents a student with a private ID, public name, protected
     * birthdate, and a list of enrolled courses.
     * - `Professor`: Represents a professor with a private ID, public name,
     * protected birthdate, and a list of courses they teach.
     * - `Course`: Represents a course with a curriculum, assigned room, list of
     * students, and a professor.
     */

    /**
     * Superclass `Person` representing a person in the school.
     * - Contains fields: `id` (private), `name` (public), `birthdate` (protected)
     * LocalDate.
     * - Provides a constructor to initialize these fields in the order above.
     * - Provides getters for all fields. You should not be able to set your id,
     * name, or birthdate.
     * - Overrides `toString()` to return a string representation of the person.
     * - Must match Person[id=###, name=XYZ, birthdate=YYYY-MM-DD]
     * - id and name can be any reasonable length > 0 and will fit within their data
     * type.
     * - This goes for all fields included in toStrings
     * - where # represents a number, XYZ represents alphabetical characters, YMD is
     * year month date
     */
    public static class Person {

        private int id;

        public String name;

        protected LocalDate birthdate;

        /**
         * Constructs a new Person object with the specified id, name, and birthdate.
         *
         * @param id        The unique ID of the person
         * @param name      The person's name
         * @param birthdate The birthdate of the person (format: YYYY-MM-DD)
         */
        public Person(int id, String name, LocalDate birthdate) {
            this.id = id;
            this.name = name;
            this.birthdate = birthdate;
        }

        /**
         * Retrieves the person's ID.
         *
         * @return The integer ID of the person
         */
        public int getId() {
            return id;
        }

        /**
         * Retrieves the person's name.
         *
         * @return The name of the person
         */
        public String getName() {
            return name;
        }

        /**
         * Retrieves the person's birthdate.
         *
         * @return The LocalDate representing the birthdate
         */
        public LocalDate getBirthdate() {
            return birthdate;
        }

        /**
         * Returns a string representation of the person object.
         * Format: Person[id=###, name=XYZ, birthdate=YYYY-MM-DD]
         *
         * @return Formatted string representing the person
         */
        @Override
        public String toString() {
            return String.format("Person[id=%d, name=%s, birthdate=%s]", id, name, birthdate);
        }
    }

    /**
     * Subclass `Student` representing a student.
     * - Inherits from `Person`.
     * - Adds a private list of `enrolledCourses`
     * - Constructor should continue off Person and create an empty list of enrolled
     * courses.
     * - Provides methods to enroll in and drop courses.
     * - Provides getter for enrolled courses
     * - Overrides toString()
     * - Must match Student[id=###, name=XYZ, birthdate=YYYY-MM-DD,
     * enrolledCourses=##]
     * - Same rules as above, enrolledCourses= num of enrolled courses
     */
    public static class Student extends Person {

        private List<Course> enrolledCourses;

        /**
         * Constructs a Student object using the given id, name, and birthdate.
         * Initializes the enrolledCourses list as empty.
         *
         * @param id        Unique student ID
         * @param name      Student's name
         * @param birthdate Student's date of birth
         */
        public Student(int id, String name, LocalDate birthdate) {
            super(id, name, birthdate);
            this.enrolledCourses = new ArrayList<>();
        }

        /**
         * Enrolls the student in a course if not already enrolled.
         * Also adds the student to the course's student list.
         *
         * @param course The course to enroll in
         */
        public void enroll(Course course) {
            if (!enrolledCourses.contains(course)) {
                enrolledCourses.add(course);
                course.addStudent(this);
            }
        }

        /**
         * Drops the student from a course if currently enrolled.
         * Also removes the student from the course's student list.
         *
         * @param course The course to drop
         */
        public void drop(Course course) {
            if (enrolledCourses.contains(course)) {
                enrolledCourses.remove(course);
                course.removeStudent(this);
            }
        }

        /**
         * Returns the list of courses the student is currently enrolled in.
         *
         * @return List of enrolled courses
         */
        public List<Course> getEnrolledCourses() {
            return enrolledCourses;
        }

        /**
         * Returns a string representation of the student.
         * Format: Student[id=###, name=XYZ, birthdate=YYYY-MM-DD, enrolledCourses=##]
         *
         * @return Formatted string representing the student
         */
        @Override
        public String toString() {
            return String.format("Student[id=%d, name=%s, birthdate=%s, enrolledCourses=%d]",
                    getId(), getName(), getBirthdate(), enrolledCourses.size());
        }
    }

    /**
     * Subclass `Professor` representing a professor.
     * - Inherits from `Person`.
     * - Adds a private list of `taughtCourses`
     * - Constructor should continue off Person and create an empty list of taught
     * courses.
     * - Provides methods to add and remove courses they teach.\
     * - Provides getter for taught courses
     * - Overrides toString()
     * - Must match Student[id=###, name=XYZ, birthdate=YYYY-MM-DD,
     * taughtCourses=##]
     * - Same rules as above, taughtCourses= num of taught courses
     */
    public static class Professor extends Person {

        private List<Course> taughtCourses;

        /**
         * Constructs a Professor object using the given id, name, and birthdate.
         * Initializes the taughtCourses list as empty.
         *
         * @param id        Unique professor ID
         * @param name      Professor's name
         * @param birthdate Professor's date of birth
         */
        public Professor(int id, String name, LocalDate birthdate) {
            super(id, name, birthdate);
            this.taughtCourses = new ArrayList<>();
        }

        /**
         * Adds a course to the professor's list of taught courses if not already
         * present.
         * Also sets this professor as the course's assigned professor.
         *
         * @param course The course to add
         */
        public void addCourse(Course course) {
            if (!taughtCourses.contains(course)) {
                taughtCourses.add(course);
                course.setProfessor(this);
            }
        }

        /**
         * Removes a course from the professor's list of taught courses if present.
         * Also removes the professor from the course.
         *
         * @param course The course to remove
         */
        public void removeCourse(Course course) {
            if (taughtCourses.contains(course)) {
                taughtCourses.remove(course);
                course.removeProfessor();
            }
        }

        /**
         * Returns the list of courses this professor is currently teaching.
         *
         * @return List of taught courses
         */
        public List<Course> getTaughtCourses() {
            return taughtCourses;
        }

        /**
         * Returns a string representation of the professor.
         * Format: Professor[id=###, name=XYZ, birthdate=YYYY-MM-DD, taughtCourses=##]
         *
         * @return Formatted string representing the professor
         */
        @Override
        public String toString() {
            return String.format("Professor[id=%d, name=%s, birthdate=%s, taughtCourses=%d]",
                    getId(), getName(), getBirthdate(), taughtCourses.size());
        }
    }

    /**
     * Class `Course` representing a course.
     * - Contains all private fields: `curriculum` (String), `assignedRoom`
     * (String), `students` (List<Student>), `professor` (Professor).
     * - Constructor takes in two args: String curriculum, String assignedRoom
     * - Also sets an empty list of students and a placeholder value for professor
     * - Provides methods to add/remove students and set/remove the professor.
     */
    public static class Course {

        private String curriculum;

        private String assignedRoom;

        private List<Student> students;

        private Professor professor;

        /**
         * Constructs a Course object with the given curriculum name and assigned room.
         * Initializes an empty list of students and sets the professor as null.
         *
         * @param curriculum   The curriculum name of the course
         * @param assignedRoom The room where the course takes place
         */
        public Course(String curriculum, String assignedRoom) {
            this.curriculum = curriculum;
            this.assignedRoom = assignedRoom;
            this.students = new ArrayList<>();
            this.professor = null;
        }

        /**
         * Adds a student to the course's student list if not already enrolled.
         *
         * @param student The student to add
         */
        public void addStudent(Student student) {
            if (!students.contains(student)) {
                students.add(student);
            }
        }

        /**
         * Removes a student from the course's student list if enrolled.
         *
         * @param student The student to remove
         */
        public void removeStudent(Student student) {
            students.remove(student);
        }

        /**
         * Assigns a professor to the course.
         *
         * @param professor The professor to assign
         */
        public void setProfessor(Professor professor) {
            this.professor = professor;
        }

        /**
         * Removes the currently assigned professor from the course.
         */
        public void removeProfessor() {
            this.professor = null;
        }

        /**
         * Returns the curriculum name of the course.
         *
         * @return The curriculum name
         */
        public String getCurriculum() {
            return curriculum;
        }

        /**
         * Returns the assigned room for the course.
         *
         * @return The room name
         */
        public String getAssignedRoom() {
            return assignedRoom;
        }

        /**
         * Returns the list of students currently enrolled in the course.
         *
         * @return List of enrolled students
         */
        public List<Student> getStudents() {
            return students;
        }

        /**
         * Returns the professor assigned to the course (or null if none).
         *
         * @return Assigned professor or null
         */
        public Professor getProfessor() {
            return professor;
        }

        /**
         * Returns a string representation of the course.
         *
         * @return Formatted string representing the course
         */
        @Override
        public String toString() {
            return String.format("Course[curriculum=%s, room=%s, students=%d, professor=%s]",
                    curriculum, assignedRoom, students.size(),
                    professor != null ? professor.getName() : "None");
        }
    }

    /**
     * Problem 2: Shape Hierarchy with Abstract Classes and Generics
     *
     * Implement an abstract class `Shape<T extends Number>` that implements the
     * `AreaCalculable<T>` interface.
     * Add an abstract method `calcPerimeter()` to calculate the perimeter of the
     * shape.
     * Create concrete classes `Circle`, `Triangle`, and `Rectangle` that extend
     * `Shape<T>`.
     */

    /**
     * Interface `AreaCalculable<T>` defines a method calculateArea() that should
     * return a double.
     */
    public interface AreaCalculable<T extends Number> {
        double calculateArea();
    }

    /**
     * Abstract class `Shape<T>` represents a geometric shape.
     * - Implements the `AreaCalculable<T>` interface.
     * - Contains a protected field `unit` of type `T` to represent the unit of
     * measurement.
     * - Provides a constructor to initialize the unit.
     * - Provides getters and setters for the unit.
     * - Adds a public abstract method `calcPerimeter()` which should return a
     * double.
     */
    public abstract static class Shape<T extends Number> implements AreaCalculable<T> {
        // Constructor
        protected T unit;

        public Shape(T unit) {
            this.unit = unit;
        }

        // Getters and Setters
        public T getUnit() {
            return unit;
        }

        public void setUnit(T unit) {
            this.unit = unit;
        }

        // Abstract method to calculate the perimeter of the shape
        public abstract double calcPerimeter();
    }

    /**
     * Class `Circle` represents a circle.
     * - Extends `Shape<T>`.
     * - Adds a private field `radius` of type `T`.
     * - Constructor should take in two args in order: T radius, T unit
     * - Provide getters and setters for `radius`.
     * - Implement the `calculateArea()` method for a circle.
     * - Implement the `calcPerimeter()` method for a circle.
     * - Override the toString()
     * - Must match Circle[radius=###, unit=###]
     */
    public static class Circle<T extends Number> extends Shape<T> {

        private T radius;

        /**
         * Constructs a Circle with the specified radius and unit of measurement.
         *
         * @param radius The radius of the circle
         * @param unit   The unit of measurement (e.g., cm, m, inch)
         */
        public Circle(T radius, T unit) {
            super(unit);
            this.radius = radius;
        }

        /**
         * Returns the radius of the circle.
         *
         * @return The radius
         */
        public T getRadius() {
            return radius;
        }

        /**
         * Sets the radius of the circle.
         *
         * @param radius The new radius
         */
        public void setRadius(T radius) {
            this.radius = radius;
        }

        /**
         * Calculates the area of the circle.
         *
         * @return The area as a double
         */
        @Override
        public double calculateArea() {
            return Math.PI * Math.pow(radius.doubleValue(), 2);
        }

        /**
         * Calculates the perimeter (circumference) of the circle.
         *
         * @return The perimeter as a double
         */
        @Override
        public double calcPerimeter() {
            return 2 * Math.PI * radius.doubleValue();
        }

        /**
         * Returns a string representation of the circle.
         *
         * @return Formatted string
         */
        @Override
        public String toString() {
            return String.format("Circle[radius=%.2f, unit=%.2f]",
                    radius.doubleValue(), unit.doubleValue());
        }
    }

    /**
     * Class `Triangle` represents a triangle.
     * - Extends `Shape<T>`.
     * - Adds private fields `base`, `height`, and `side` of type `T`.
     * - Constructor takes in: T base, T height, T side, T unit
     * - Provides getters and setters for `base`, `height`, and `side`.
     * - Implements the `calculateArea()` method for a triangle.
     * - Implements the `calcPerimeter()` method for a triangle.
     * - Overrides toString()
     * - Must match Triangle[base=###, height=###, side=###, unit=###]
     */
    public static class Triangle<T extends Number> extends Shape<T> {

        private T base;

        private T height;

        private T side;

        /**
         * Constructs a Triangle with given base, height, side, and unit of measurement.
         *
         * @param base   The base length of the triangle
         * @param height The height of the triangle
         * @param side   The side length (assumed equal on both sides)
         * @param unit   The unit of measurement
         */
        public Triangle(T base, T height, T side, T unit) {
            super(unit);
            this.base = base;
            this.height = height;
            this.side = side;
        }

        /**
         * Returns the base of the triangle.
         *
         * @return The base length
         */
        public T getBase() {
            return base;
        }

        /**
         * Sets the base of the triangle.
         *
         * @param base The new base length
         */
        public void setBase(T base) {
            this.base = base;
        }

        /**
         * Returns the height of the triangle.
         *
         * @return The height
         */
        public T getHeight() {
            return height;
        }

        /**
         * Sets the height of the triangle.
         *
         * @param height The new height
         */
        public void setHeight(T height) {
            this.height = height;
        }

        /**
         * Returns the side length of the triangle.
         *
         * @return The side length
         */
        public T getSide() {
            return side;
        }

        /**
         * Sets the side length of the triangle.
         *
         * @param side The new side length
         */
        public void setSide(T side) {
            this.side = side;
        }

        /**
         * Calculates the area of the triangle using the formula:
         *
         * @return The area as a double
         */
        @Override
        public double calculateArea() {
            return 0.5 * base.doubleValue() * height.doubleValue();
        }

        /**
         * Calculates the perimeter of the triangle assuming two equal sides:
         *
         * @return The perimeter as a double
         */
        @Override
        public double calcPerimeter() {
            return base.doubleValue() + side.doubleValue() * 2;
        }

        /**
         * Returns a string representation of the triangle.
         *
         * @return Formatted string
         */
        @Override
        public String toString() {
            return String.format("Triangle[base=%.2f, height=%.2f, side=%.2f, unit=%.2f]",
                    base.doubleValue(), height.doubleValue(), side.doubleValue(), unit.doubleValue());
        }
    }

    /**
     * Class `Rectangle` represents a rectangle.
     * - Extends `Shape<T>`.
     * - Adds private fields `length` and `width` of type `T`.
     * - Constructor takes in: T length, T width, T unit
     * - Provides getters and setters for `length` and `width`.
     * - Implements the `calculateArea()` method for a rectangle.
     * - Implements the `calcPerimeter()` method for a rectangle.
     * - Override toString()
     * - Must match Rectangle[length=###, width=###, unit=###]
     */
    public static class Rectangle<T extends Number> extends Shape<T> {

        private T length;

        private T width;

        /**
         * Constructs a Rectangle with the given length, width, and unit of measurement.
         *
         * @param length The length of the rectangle
         * @param width  The width of the rectangle
         * @param unit   The unit of measurement (e.g., cm, m)
         */
        public Rectangle(T length, T width, T unit) {
            super(unit);
            this.length = length;
            this.width = width;
        }

        /**
         * Returns the length of the rectangle.
         *
         * @return The length
         */
        public T getLength() {
            return length;
        }

        /**
         * Sets the length of the rectangle.
         *
         * @param length The new length
         */
        public void setLength(T length) {
            this.length = length;
        }

        /**
         * Returns the width of the rectangle.
         *
         * @return The width
         */
        public T getWidth() {
            return width;
        }

        /**
         * Sets the width of the rectangle.
         *
         * @param width The new width
         */
        public void setWidth(T width) {
            this.width = width;
        }

        /**
         * Calculates the area of the rectangle.
         *
         * @return The area as a double
         */
        @Override
        public double calculateArea() {
            return length.doubleValue() * width.doubleValue();
        }

        /**
         * Calculates the perimeter of the rectangle.
         *
         * @return The perimeter as a double
         */
        @Override
        public double calcPerimeter() {
            return 2 * (length.doubleValue() + width.doubleValue());
        }

        /**
         * Returns a string representation of the rectangle.
         *
         * @return Formatted string
         */
        @Override
        public String toString() {
            return String.format("Rectangle[length=%.2f, width=%.2f, unit=%.2f]",
                    length.doubleValue(), width.doubleValue(), unit.doubleValue());
        }
    }

    /**
     * Problem 3: Employee Management System
     *
     * Implement an `Employee` class that implements `Payable`, `Trainable`, and
     * `Reportable`.
     * The `Employee` class should calculate salary based on performance and
     * maintain a list of certifications.
     */

    /**
     * Interface `Payable` defines a method to calculate salary and includes a base
     * pay constant.
     * BASE_PAY should be 50000, calculateSalary() should take in performanceScore
     * (int) and return a double
     */

    public interface Payable {
        double BASE_PAY = 50000;

        double calculateSalary(int performanceScore);
    }

    /**
     * Interface `Trainable` defines a method to add certifications.
     * addCertification() should take in certification (String) and not return
     * anything
     */
    public interface Trainable {
        void addCertification(String certification);
    }

    /**
     * Interface `Reportable` defines a method to generate a performance score.
     * generatePerformanceScore() should not take in anything and return an int
     */
    public interface Reportable {
        int generatePerformanceScore();
    }

    /**
     * Class `Employee` represents an employee in the organization.
     * - Implements `Payable`, `Trainable`, and `Reportable`.
     * - Adds private fields `name` (String), `id` (int), and `certifications` which
     * will be a list of strings
     * - You should not be able to set name, id, or certifications
     * - Constructor takes in String name, int id
     * - Starts with an empty list of certifications
     * - Implement the interface functions
     * - For `calculateSalary()` your bonus should be your base_pay *
     * (your_performance_score/100).
     * - You should return your base pay + your bonus
     * - For `addCertification()`, add in the certification
     * - For `generatePerformanceScore()`, your score should be your num of
     * certifications * 10, capped at 100
     * - Override toString()
     * - Must match Employee[name=XYZ, id=###, certifications=[...]]
     * - fields can be any length as with all other methods; certifications should
     * show all of your certifications
     */
    public static class Employee implements Payable, Trainable, Reportable {

        private String name;

        private int id;

        private List<String> certifications;

        /**
         * Constructs an Employee with a specified name and ID.
         *
         * @param name Employee's name
         * @param id   Employee's unique identifier
         */
        public Employee(String name, int id) {
            this.name = name;
            this.id = id;
            this.certifications = new ArrayList<>();
        }

        /**
         * Returns the name of the employee.
         *
         * @return Employee's name
         */
        public String getName() {
            return name;
        }

        /**
         * Returns the employee's ID.
         *
         * @return Employee's ID
         */
        public int getId() {
            return id;
        }

        /**
         * Returns a list of all certifications the employee has.
         *
         * @return List of certification strings
         */
        public List<String> getCertifications() {
            return certifications;
        }

        /**
         * Adds a new certification to the employee's record.
         *
         * @param certification The certification to add
         */
        @Override
        public void addCertification(String certification) {
            certifications.add(certification);
        }

        /**
         * Generates a performance score based on number of certifications.
         *
         * @return Performance score (0–100)
         */
        @Override
        public int generatePerformanceScore() {
            return Math.min(certifications.size() * 10, 100);
        }

        /**
         * Calculates salary based on performance score.
         *
         * @param performanceScore A value between 0 and 100
         * @return Total salary as a double
         */
        @Override
        public double calculateSalary(int performanceScore) {
            return BASE_PAY + (BASE_PAY * performanceScore / 100.0);
        }

        /**
         * Returns a string representation of the employee.
         *
         * @return Formatted string of employee data
         */
        @Override
        public String toString() {
            return String.format("Employee[name=%s, id=%d, certifications=%s]",
                    name, id, certifications);
        }
    }

    public static void main(String[] args) {
        // --------- Problem 1: School Hierarchy ----------
        Student s1 = new Student(1, "Hogan", LocalDate.of(2000, 1, 15));
        Student s2 = new Student(2, "Bob", LocalDate.of(1999, 5, 20));
        Professor prof1 = new Professor(100, "Smith", LocalDate.of(1975, 6, 10));

        Course course1 = new Course("Math 101", "Room A");
        Course course2 = new Course("Physics 201", "Room B");

        // Students enroll
        s1.enroll(course1);
        s2.enroll(course1);
        s1.enroll(course2);

        // Professor teaches
        prof1.addCourse(course1);
        prof1.addCourse(course2);

        System.out.println(s1); // Should show 2 enrolledCourses
        System.out.println(s2); // Should show 1 enrolledCourse
        System.out.println(prof1); // Should show 2 taughtCourses
        System.out.println(course1); // Should list 2 students, 1 professor

        // Drop one course
        s1.drop(course1);
        prof1.removeCourse(course2);

        System.out.println("\nAfter dropping and removing:");
        System.out.println(s1); // Should show 1 course
        System.out.println(course1); // Should show 1 student
        System.out.println(course2); // Should have no professor

        // --------- Problem 1: Second School Hierarchy ----------
        Student s3 = new Student(3, "Alice", LocalDate.of(2001, 3, 14));
        Professor prof2 = new Professor(101, "David", LocalDate.of(1980, 12, 5));
        Course course3 = new Course("Biology 301", "Room C");

        // Enroll same student multiple times
        s3.enroll(course3);
        s3.enroll(course3); // Should not duplicate
        System.out.println(course3); // Should show 1 student

        // Add same professor multiple times
        prof2.addCourse(course3);
        prof2.addCourse(course3); // Should not duplicate
        System.out.println(prof2); // Should show 1 taught course

        // Drop and re-enroll
        s3.drop(course3);
        System.out.println("After drop: " + s3); // Should show 0 enrolledCourses
        s3.enroll(course3);
        System.out.println("Re-enrolled: " + s3); // Should show 1 enrolledCourse

        // Remove professor and reassign
        course3.removeProfessor();
        System.out.println("After professor removed: " + course3);
        course3.setProfessor(prof1);
        System.out.println("Professor reassigned: " + course3);

        // --------- Problem 2: Shape Hierarchy ----------
        Circle<Double> circle = new Circle<>(5.0, 1.0);
        Triangle<Double> triangle = new Triangle<>(3.0, 4.0, 5.0, 1.0);
        Rectangle<Double> rectangle = new Rectangle<>(4.0, 6.0, 1.0);

        System.out.println(circle);
        System.out.printf("Area: %.2f, Perimeter: %.2f\n", circle.calculateArea(), circle.calcPerimeter());

        System.out.println(triangle);
        System.out.printf("Area: %.2f, Perimeter: %.2f\n", triangle.calculateArea(), triangle.calcPerimeter());

        System.out.println(rectangle);
        System.out.printf("Area: %.2f, Perimeter: %.2f\n", rectangle.calculateArea(), rectangle.calcPerimeter());

        // Circle with radius = 0
        Circle<Double> zeroCircle = new Circle<>(0.0, 1.0);
        System.out.println(zeroCircle);
        System.out.printf("Area: %.2f, Perimeter: %.2f\n", zeroCircle.calculateArea(), zeroCircle.calcPerimeter());

        // Triangle with decimal values
        Triangle<Double> decimalTriangle = new Triangle<>(3.3, 4.4, 5.5, 0.1);
        System.out.println(decimalTriangle);
        System.out.printf("Area: %.2f, Perimeter: %.2f\n", decimalTriangle.calculateArea(),
                decimalTriangle.calcPerimeter());

        // Rectangle with large numbers
        Rectangle<Integer> bigRectangle = new Rectangle<>(1000, 2000, 1);
        System.out.println(bigRectangle);
        System.out.printf("Area: %.2f, Perimeter: %.2f\n", bigRectangle.calculateArea(), bigRectangle.calcPerimeter());

        // --------- Problem 3: Employee System ----------
        Employee emp = new Employee("Hogan Lin", 12345);
        emp.addCertification("Java");
        emp.addCertification("OOP");
        emp.addCertification("Teamwork");

        System.out.println(emp); // Should list 3 certifications
        int score = emp.generatePerformanceScore();
        double salary = emp.calculateSalary(score);

        System.out.printf("Performance Score: %d\n", score); // Should be 30
        System.out.printf("Calculated Salary: %.2f\n", salary); // BASE + 30%

        Employee emp2 = new Employee("Hung Lin", 54321);

        // Add no certifications
        System.out.println(emp2); // Empty cert list
        System.out.println("Performance Score (0 certs): " + emp2.generatePerformanceScore());
        System.out.println("Salary: " + emp2.calculateSalary(emp2.generatePerformanceScore()));

        // Add 11 certs (should cap at 100)
        for (int i = 1; i <= 11; i++) {
            emp2.addCertification("Cert" + i);
        }
        System.out.println(emp2); // Should show 11 certs
        System.out.println("Performance Score (capped): " + emp2.generatePerformanceScore()); // Should be 100
        System.out.println("Salary (max): " + emp2.calculateSalary(emp2.generatePerformanceScore())); // Should be
                                                                                                      // 100,000
    }
}