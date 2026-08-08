'''
Exercise 5: Pipeline Health Status
Student: Agrim Shiwakoti
Day: 1
'''

#Input Values
rows_loaded = 9900
rows_failed = 100
runtime_minutes = 18


#calculations
failure_rate = (rows_failed / (rows_loaded + rows_failed)) * 100
long_runtime_flag = False
#logics
if runtime_minutes > 20:
    long_runtime_flag = True

if (failure_rate <= 2 and runtime_minutes <= 20) or (failure_rate <= 2):
    status = "Healthy"
elif failure_rate <= 5:
    status = "Warning"
else:
    status = "Critical"

final_status = status + (" - Long Runtime" if long_runtime_flag else "") #printing for long runtime

#Output
print(f"Rows Loaded: {rows_loaded}")
print(f"Rows Failed: {rows_failed}")
print(f"Runtime (minutes): {runtime_minutes}")
print(f"Failure Rate: {failure_rate:.2f}%")
print(f"Pipeline Status: {final_status}")