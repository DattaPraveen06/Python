# 1)The Corporation has listed the requirement for shortling the candidates for a worker’s job. The conditions are as under:
#
# Applicant should be male
# Applicants should be between 20 and 25 years of age.
# Applicants should have been born after 2024 January 1
#
# If the applicant meets the above condition, display the message “Shortlisted”. Else display “Not Shortlisted”
#
# Accept the details of gender (M/F), age (in years) and date or birth (dd/mm/yyyy) from the user.


gender = input('enter the gender: ')
age = int(input('enter the age: '))
DOB = input('enter date of birth: ')

if 20 <= age <= 25:
    if(gender == 'M'):
        print("Shortlisted")
    else:
        print("Not Shortlisted")
else:
    print("Not Shortlisted")
    
    
#-------------------OR---------------------
    
gender = input('Enter the gender (M/F): ')
age = int(input('Enter the age: '))
DOB = input('Enter date of birth: ')

shortlisted = False  # Flag to track if shortlisted

if 20 <= age <= 25:
    if gender == 'M':
        shortlisted = True

if shortlisted:
    print("Shortlisted")
else:
    print("Not Shortlisted")

    
