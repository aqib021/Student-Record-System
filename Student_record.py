class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll(self, course):
        self.courses[course.course_code] = course

    def record_grade(self, course, grade):
        if course.course_code in self.courses:
            self.courses[course.course_code].record_grade(self, grade)
        else:
            print(f"{self.name} is not enrolled in {course.course_name}")

    def display_info(self):
        print(f"\nStudent ID: {self.student_id}")
        print(f"Name: {self.name}")
        print("Enrolled Courses:")
        for course in self.courses.values():
            print(f"  {course.course_code}: {course.course_name}")

class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = {}
        self.grades = {}

    def enroll_student(self, student):
        self.students[student.student_id] = student

    def record_grade(self, student, grade):
        self.grades[student.student_id] = grade

    def display_info(self):
        print(f"\nCourse Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print("Enrolled Students:")
        if not self.students:
            print("  No students enrolled.")
        else:
            for student in self.students.values():
                print(f"  {student.student_id}: {student.name}")
            print("Grades:")
            for student_id, grade in self.grades.items():
                print(f"  {student_id}: {grade}")

def welcome_message():
    print("Welcome to the Student Record System!")

def display_options():
    print("\nOptions:")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. Record Grade")
    print("5. Display Student Information")
    print("6. Display Course Information")
    print("7. Exit")

def initialize_example_data(students, courses):
    # Example data
    students_data = {
        101: {"name": "Alex"},
        115: {"name": "Bob"},
        125: {"name": "Joe"}
    }

    courses_data = {
        "CSE101": {"name": "Introduction to Programming"},
        "CSE110": {"name": "Computer Architecture"},
        "MAT120": {"name": "Linear Algebra"}
    }

    # Initialize courses first
    for course_code, data in courses_data.items():
        course = Course(course_code, data["name"])
        courses[course_code] = course

    # Then initialize students
    for student_id, data in students_data.items():
        student = Student(student_id, data["name"])
        students[student_id] = student
        # Automatically enroll each student in CSE101
        course_cse101 = courses["CSE101"]
        student.enroll(course_cse101)
        course_cse101.enroll_student(student)

    # Initialize courses
    for course_code, data in courses_data.items():
        courses[course_code] = Course(course_code, data["name"])

def main():
    students = {}
    courses = {}

    welcome_message()

    # Initializing here with example data
    initialize_example_data(students, courses)

    while True:
        display_options()

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            students[student_id] = Student(student_id, name)
            print(f"{name} has been added to the system.")

        elif choice == "2":
            course_code = input("Enter course code: ")
            course_name = input("Enter course name: ")
            courses[course_code] = Course(course_code, course_name)
            print(f"Course {course_name} has been added to the system.")

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            course_code = input("Enter course code: ")

            if student_id in students and course_code in courses:
                students[student_id].enroll(courses[course_code])
                courses[course_code].enroll_student(students[student_id])
                print(f"{students[student_id].name} has been enrolled in {courses[course_code].course_name}")
            else:
                print("Invalid student ID or course code. Please ensure both exist in the system.")

        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            course_code = input("Enter course code: ")
            grade = input("Enter grade: ")

            if student_id in students and course_code in courses:
                students[student_id].record_grade(courses[course_code], grade)
                print(f"Grade recorded for {students[student_id].name} in {courses[course_code].course_name}")
            else:
                print("Invalid student ID or course code. Please ensure both exist in the system.")

        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            if student_id in students:
                students[student_id].display_info()
            else:
                print("Invalid student ID. Please ensure it exists in the system.")

        elif choice == "6":
            course_code = input("Enter course code: ")
            if course_code in courses:
                courses[course_code].display_info()
            else:
                print("Invalid course code. Please ensure it exists in the system.")

        elif choice == "7":
            print("Thank you for using the Student Record System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
