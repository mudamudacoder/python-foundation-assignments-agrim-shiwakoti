'''
Exercise 1: Batch Processor
Student: Agrim Shiwakoti
Day: 2
'''

batch_number = 1  #starting value 

for batch_number in range(1, 11): #range is inclusive of 1 and exclusive of 11, so it will process batches 1 to 10
    print(f"Processing batch number: {batch_number}")
    
    if batch_number % 3 == 0: #checking if multiple of 3
        print("Checkpoint reached")
