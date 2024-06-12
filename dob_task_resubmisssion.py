# Retrieve the data from DOB.txt file
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

# Function to separate the names from the date of birth
def separate_name_and_dob(data):
    names_dobs = []
    for line in data:
        # Strip the trailling whitespaces
        line = line.strip()
        # Split the line at spaces
        parts = line.split(' ')
        # Join all parts except the last three to form the name
        name = ' '.join(parts[:-3])
        # Join the last three parts to form the date of birth
        dob = ' '.join(parts[-3:])
        names_dobs.append((name, dob))
    return names_dobs

if __name__ == "__main__":
    file_path = "/Users/brianawilson/Documents/Coding Tasks Submissions/Task 8/DOB.txt" 
    data = read_data(file_path)
    names_dobs = separate_name_and_dob(data)
    
    # Prints out the names
    print("Names:")
    for name_dob in names_dobs:
        print(name_dob[0])
    
    # Prints the dates of birth
    print("\nDates of Birth:")
    for name_dob in names_dobs:
        print(name_dob[1])