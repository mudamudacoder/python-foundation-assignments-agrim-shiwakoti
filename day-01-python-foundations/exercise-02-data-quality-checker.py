'''
Exercise 2: Data Quality Checker
Student: Agrim Shiwakoti
Day: 1
'''
#Input values
total_rows = 2000
missing_rows = 120
duplicate_rows = 30


#calculating total num of problematic rows and percentage
problematic_rows = missing_rows + duplicate_rows #assuming missing and duplicate rows dont overlap

problematic_rows_percentage = (problematic_rows / total_rows) * 100

#logic for classification based on percentage of problematic rows
if problematic_rows_percentage <= 2:
  classification = "Excellent"
elif problematic_rows_percentage <=5:
  classification = "Acceptable"
else:
  classification = "Needs Cleaning"

#Output
print(f"Total Rows::: {total_rows}")
print(f"Problematic Rows::: {problematic_rows}")
print(f"Problematic Percentage::: {problematic_rows_percentage}")
print(f"Classification::: {classification}")