# 1) The Corporation has listed the requirement for shortling the candidates for a worker’s job. The conditions are as under:

# Applicant should be male
# Applicants should be between 20 and 25 years of age.
# Applicants should have been born after 2024 January 1
# If the applicant meets the above condition, display the message “Shortlisted”. Else display “Not Shortlisted”
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

#----------------------------------------------------------------------------------------------------

# 4) Create a new string made of the first, middle, and last characters of each input string

string = input('enter a string:')
s1 = string[0]
s2 = string[-1]
l = len(string)
if l%2 ==1:
    l1 = l/2
else:
    l1 = l/2 - 1

s3 = string[int(l1)]
print(f'first: {s1} , middle: {s3}, last: {s2}')

#----------------------------------------------------------------------------------------------------
# 5) Reverse a given string

original = "Hello, World!"
reversed= original[::-1]
print(reversed)

#----------------------------------------------------------------------------------------------------


# 6) Given two strings, s1 and s2. Write a program to create a new string s3
# made of the first char of s1, then the last char of s2, Next, the second char of s1
# and second last char of s2, and so on. Any leftover chars go at the end of the result.

s1 = 'hello'
s2 = 'worlds'

s3 = ''
i = 0
l = len(s2)

while i < len(s1) and i < l:
    s3 += s1[i] + s2[-(i + 1)]  # s2[-(i + 1)] gives the character from the end of s2
    i += 1

# Append any remaining characters from s1
if i < len(s1):
    s3 += s1[i:]

# Append any remaining characters from s2
if i < l:
    s3 += s2[:l - i]

print(s3)

#--------------------------------------------------------------------------------------------------------------

#7) Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = 'Hello world'
s2 = 'Beautiful'
s3 = s1.split(' ')
s3 = s3[0] + ' ' + s2 + ' ' + s3[1]
print(s3)


