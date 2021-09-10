
import csv

def get_list (file_path):
    with open('Employee_information.csv', 'r') as csvfile :
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        print(reader_list)
        return len(reader_list)

def append_to_Employee_information(file_path, Full_name, Employee_ID, Email, Contact, Nationality, Preferred_mode_of_contact):
    
    fieldname=['number', 'Full_name', 'Employee_ID', 'Email', 'Contact', 'Nationality', 'Preferred_mode_of_contact']
    next_id = get_list(file_path)
    with open(file_path, 'a') as csvfile:
       
        writer = csv.DictWriter(csvfile, fieldnames= fieldname)
        writer.writeheader()
        writer.writerow({
            'number':next_id,
            'Full_name': Full_name,
            'Employee_ID': Employee_ID,
            'Email': Email,
            'Contact': Contact, 
            'Nationality': Nationality,
            'Preferred_mode_of_contact': Preferred_mode_of_contact})
         
append_to_Employee_information(
'Employee_information.csv', 
'Astha Budhathoki',
'110', 
'xyz@gmail.com', 
'000-111-0000', 'Nepal', 'Email')
