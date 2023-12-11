# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions with structured error handling
# Change Log: (Who, When, What)
#   Sam Bircher, 12/10/23,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.



#Processing---------------------------------------#
class FileProcessor:
    """
        A collection of processing layer functions that work with Json files

        ChangeLog: (Who, When, What)
        Sam Bircher, 12/10/23, Created script
        """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        When the program starts, read the file data into a list of lists (table)

        Change Log: (Who, When, What)
        Sam Bircher, 12/10/23, Created script

        :param file_name:
        :param student_data:
        :return: student_data
        """
        try:
            with open(file_name, "r") as file:
                student_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return student_data
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes data to the specified JSON file

        Change Log: (Who, When, What)
        Sam Bircher, 12/10/23, Created script

        :param file_name:
        :param student_data:
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

#Presentation-------------------------------------#
class IO:
    """
        A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        Sam Bircher, 12/10/23, Created script
        """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays custom error messages to the user

        ChangeLog: (Who, When, What)
        Sam Bircher, 12/10/23, Created script

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Sam Bircher, 12/10/23, Created script

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Sam Bircher, 12/10/23, Created script

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        Sam Bircher, 12/10/23, Created script

        :return: None
        """

        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("What is the course's name? ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)

        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function prints a list of students and their respective courses

        ChangeLog: (Who, When, What)
        Sam Bircher, 12/10/23, Created script

        :return: None
        """
        print()
        print("-" * 50)
        for student in student_data:
            print(student["FirstName"], student["LastName"], student["CourseName"])
        print("-" * 50)
        print()

while True:

    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2": #Display current data
        students=FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop


