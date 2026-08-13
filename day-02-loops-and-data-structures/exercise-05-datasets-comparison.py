'''
Exercise 5: Datasets Comparison
Student: Agrim Shiwakoti
Day: 2
'''
# input values
dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# set operations
unique_datasets = dataset_a.union(dataset_b)
common_datasets = dataset_a.intersection(dataset_b)
datasets_only_in_a = dataset_a.difference(dataset_b)
datasets_only_in_b = dataset_b.difference(dataset_a)

# Output
print(f"Unique Datasets: {unique_datasets}")
print(f"Common Datasets: {common_datasets}")
print(f"Datasets Only in Dataset A: {datasets_only_in_a}")
print(f"Datasets Only in Dataset B: {datasets_only_in_b}")