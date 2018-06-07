import java.io.*;

public class Employee{

  String name;
  Integer age;
  String designation;
  Double salary;

  public Employee(String empName) {
    this.name = empName;
  }

  public void empAge(int empAge) {
    age = empAge;
  }

  public void empDesignation(String empDesig) {
    designation = empDesig;
  }

  public void empSalary(Double empSalary) {
    salary = empSalary;
  }

  public void printEmployee() {
    System.out.println("Name: " + name);
    System.out.println("Age: " + age);
    System.out.println("Designation: " + designation);
    System.out.println("Salary: " + salary);
  }
}
