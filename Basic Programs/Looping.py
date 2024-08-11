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

#----------------------------------------------------------------------------------------------------
    
# 2)Write a program to determine the eligibility of the candidates for the position of Receptionist.

# Applicant should not be married, should be Female, should be less than 30 years
# or age and should not have more than 1 years experience.


gender = input('Enter gender: ')
age = int(input('Enter age: '))
married = input('Y or N: ')
experience = int(input('Enter work exp: '))

if gender == 'F' and age <= 30 and experience <= 1 and married == 'N':
    print("You are eligible")
else:
    print("You are Not eligible")

#----------------------------------------------------------------------------------------------------

# 3)The company is planning to give hike in salaries to its employees. The following are the conditions.

# If the employee is manager the hike is 10%
# If the employee is not a manager the hike is 20%
# Accept the salary and the position (Manager /Others), calculate the hike and display the new salary

position = input('enter your position: ')
sal = int(input('enter salary: '))

if(position == 'manager'):
    hike = sal * 0.10
else:
    hike = sal * 0.20

print(f'Your New sal = {int(sal+hike)}')
