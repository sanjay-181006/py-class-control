# Class Control System (Mini Project)

## Overview
The **Class Control System** is a Python mini project designed to demonstrate core **Object-Oriented Programming (OOP)** concepts such as abstraction, inheritance, encapsulation, and operator overloading.  
It simulates a basic school environment for managing students and their enrolled courses.

---

## Objectives
- Implement abstract base classes using `ABC`
- Demonstrate inheritance and method overriding
- Apply encapsulation for secure data handling
- Manage student records within a school system
- Practice operator overloading in Python

---

## Technologies Used
- **Language:** Python
- **Concepts:**
  - Object-Oriented Programming (OOP)
  - Abstract Base Classes
  - Encapsulation
  - Operator Overloading

---

## Project Structure

### 1. Person (Abstract Class)
- Acts as a base class for all persons
- Stores common attributes:
  - `name`
  - `id`
- Enforces implementation of `get_info()`

### 2. Student (Derived Class)
- Inherits from `Person`
- Manages a private list of courses
- Supports:
  - Adding courses
  - Removing courses
  - Combining courses using `+` operator

### 3. School
- Manages student records
- Allows searching students by ID

---

## Features
- Encapsulation of student course data
- Operator overloading to merge course lists
- Search students by unique ID
- Clean and modular OOP-based design

---

# Future Scope

The Class Control System can be expanded into a complete academic or enterprise-level
application by implementing the following improvements:

## Planned Improvements
- Teacher and Administrator modules
- Authentication and access control
- Attendance and grading systems
- Student performance analytics
- Web or desktop based interface

These improvements will make the system suitable for real-world educational institutions.

---

## ▶️ Example Usage

```python
s1 = Student("Alice", 101)
s1.add_course("Math")
s1.add_course("Physics")

s2 = Student("Bob", 102)
s2.add_course("Chemistry")

combined = s1 + s2

school = School()
school.add_student(s1)
school.add_student(s2)

print(combined.get_info())
