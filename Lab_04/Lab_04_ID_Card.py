#Kristen Ching
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
title = input("Enter your title: ")
school = input("Enter the school site: ")
schoolYear = input("Enter the school year: ")
subject = input("What is your subject? ")

def IDCard(first, last):
    print("* {:^15}" "{:^16} *".format(first,last))
print("*"*35) 
IDCard(school, schoolYear)
IDCard(firstName, lastName)
IDCard(title, subject)
print("*"*35)
