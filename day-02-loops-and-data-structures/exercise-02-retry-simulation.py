'''
Exercise 2: Retry Simulation
Student: Agrim Shiwakoti
Day: 2
'''

#input values
attempt = 1
max_attempts = 3
operation_successful = False

#processing logic
while attempt <= max_attempts and not operation_successful:
    print(f"Attempt {attempt}: Performing operation...")
    
    # Simulating operation success on the second attempt
    # if attempt == 2:
    #     operation_successful = True
    #     print("Operation successful!")
    #     break
    # else:
    #     print("Operation failed. Retrying...")
    
# uncomment the above block to simulate success on the second attempt
    
    attempt += 1
print("Operation failed after maximum attempts.")