This project consists of two main functionalities, firstly retrieving and processing names from the DOB.txt file and then registering student IDs and writing them to a separate file for further processing or record keeping. 

Features

1. Reading and Processing Data from DOB.txt
Input File: The DOB.txt file should contain lines where each line consists of a name followed by a date of birth.
Output: The script prints the names and dates of birth separately.
2. Registering Student IDs
Input: The user is prompted to enter the number of students to be registered and their respective IDs via the command line.
Output File: The reg_form.txt file will contain the student IDs followed by a line of dots for manual signing.

Functions: 

* read_data(file_path)
Reads and returns the content of the specified file.

* separate_name_and_dob(data)
Processes the data, separating names and dates of birth.

* register_students(num_students)
Prompts the user to input the specified number of student IDs.

* write_to_file(file_path, student_ids)
Writes the student IDs to the specified file, appending a line of dots for each ID.
