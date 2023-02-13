"""
Student Management System
Author: Dickson Agbemazi
"""


class StudentManagementSystem:

    student_db = {}

    def __init__(self, id, full_name, major, class_of) -> None:
        self.id = id
        self.full_name = full_name
        self.major = major
        self.class_of = class_of

    def add(self):

        self.student_db[self.id] = [self.full_name, self.major, self.class_of]
        print(f"Added {self.full_name} succesfully!")

    def delete_user(self):
        confirm_deletion = input("Do you want to delete student? (y/N): ")
        if confirm_deletion.startswith("y"):
            try:
                del self.student_db[self.id]
                print("Student deleted successfully")
            except KeyError:
                print("Student not in DB")

    def search_student(self):
        found_student = self.student_db[self.id]
        name, major, class_of = found_student
        print(f"{self.id} {name} {major} {class_of}")

    def display_students(self):
        for key, value in self.student_db.items():
            full_name, major, class_of = value
            print("  ID  | ")
            print(f"{key} {full_name} {major} {class_of}")
