'''
Exercise 4: Customer Record Cleaner
Student: Agrim Shiwakoti
Day: 1
'''

#Input Values
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

#Cleaning and formatting the input values
clean_name = raw_name.strip().title()
clean_city = raw_city.strip().title()
clean_email = raw_email.strip().lower()


#Determining the status based on age
status = "Adult" if int(raw_age) >= 18 else "Minor"


#Output
print(f"Name: {clean_name}")
print(f"City: {clean_city}")
print(f"Age: {int(raw_age)}")
print(f"Email: {clean_email}")
print(f"Status: {status}")