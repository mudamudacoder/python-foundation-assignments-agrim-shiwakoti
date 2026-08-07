'''
Exercise 3: File Validator
Student: Agrim Shiwakoti
Day: 1
'''

#Input Values
file_name = input("Enter a file name:::")

accepted_xtns = ["csv", "json", "parquet"] #making a list of accepted file types

#Processing the user input
file_name = file_name.strip().lower()

if "." not in file_name: #checking if the file name contains a file extension
  print("Invalid file name! File name must contain a file extension.")
  exit()


file_extension = file_name.split(".")[1] # taking the second element after splitting on "."


#logic to check and print the result if the file extension is in the list of accepted file types
if file_extension in accepted_xtns:
  print(f"File validated! .{file_extension} file type is accepted.")
else:
  print(f"Invalid file type! .{file_extension} file type is not accepted.")