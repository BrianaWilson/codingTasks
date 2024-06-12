#Function to register student's ID's from user input
def register_students(num_students):
    student_ids = [] #Variable to store student's ID
    for i in range(num_students):
        student_id = input(f"Enter Student ID {i+1}: ") #Asks for each student's ID 
        student_ids.append(student_id) #Adds ID to the varibale student_ids
    return student_ids

#Function to write the student's IDs in a separate form
def write_to_file(file_path, student_ids):
    with open(file_path, 'w') as file: #Creates file to write the ID's to
        for student_id in student_ids:
            file.write(student_id + '  .........' + '\n') #'....' for students to sign

#Prompts user to enter the number of students they are registering 
if __name__ == "__main__":
    num_students = int(input("How many students are registering? "))
    student_ids = register_students(num_students)
    write_to_file("reg_form.txt", student_ids) #Sends student's ID's to reg_form.txt
    print("Registration completed. Student IDs registered to reg_form.txt.")
