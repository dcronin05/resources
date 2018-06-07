import java.io.*;

public class EmployeeTest {

  public static void main(String args[]) {
    Employee empOne = new Employee("David");
    Employee empTwo = new Employee("Daniel");

    empOne.empAge(35);
    empOne.empDesignation("Fuck Face");
    empOne.empSalary(190000.10);
    empOne.printEmployee();

    empTwo.empAge(78);
    empTwo.empDesignation("Good Guy");
    empTwo.empSalary(1874830.10);
    empTwo.printEmployee();
  }
}
