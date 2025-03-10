# Create tuples to store student information
from itertools import count

student1 = ("Emily Smith", 17, "Grade 11")
student2 = ("Jack Matthews", 18, "Grade 12")
student3 = ("Naomi Jones", 16, "Grade 10")

# Create a tuple of student records
students = (student1, student2, student3)

# Use tuple methods to count and index elements
print(f"Number of students : {len(students)}")
print(f"Index of Emily Smith: {students.index(student1)}")

# Create sets for unique student IDs and courses
student_ids = {4852, 4853, 4854}
courses = {"Maths", "English", "Science", "History" }

# Perform set operations
print(f"Student IDs : {student_ids}")
print(f"Courses : {courses}")

new_students = {4855, 4856}
student_ids.update(new_students)
print(f"Updated Student IDs : {student_ids}")

completed_courses = {"Maths", "English"}
remaining_courses = courses - completed_courses
print(f"Remaining courses : {remaining_courses}")

# Use frozen sets
frozen_courses = frozenset(["Maths", "Science", "English", "History"])
print(f"Frozen courses : {frozen_courses}")

# Attempt to modify a frozen set (will raise an error)
# frozen_courses.add("Art") # Uncommenting this line will raise an AttributeError

# Create a frozen set of student data
frozen_student_data = frozenset(students)
print(f"Frozen student data : {frozen_student_data}")
