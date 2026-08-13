'''
Exercise 3: Clean Numeric Values
Student: Agrim Shiwakoti
Day: 2
'''

#input values
raw_list = [100, None, 250, "invalid", 300, None, 450]

new_list = [val for val in raw_list if isinstance(val, int)] #list comprehension

# for item in raw_list:
#     if not isinstance(item, int):
#         continue
#     new_list.append(item)

# uncomment above code to test for loop, continue and isinstance() function


print(new_list)