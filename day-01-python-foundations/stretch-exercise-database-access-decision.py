'''
Stretch Exercise: Database Access Decision
Student: Agrim Shiwakoti
Day: 1
'''
#Input Values
user_role = "dev"
is_active = True
requested_dataset = "financial_data"

#fixed datasets
allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]

access_granted = False

if user_role in allowed_roles and is_active and requested_dataset not in restricted_datasets:
    access_granted = True
    print("Access granted.")
elif user_role not in allowed_roles:
    access_granted = False
    print("Access denied because the role is not allowed.")
elif not is_active:
    access_granted = False
    print("Access denied because the user is inactive.")
elif requested_dataset in restricted_datasets:
    access_granted = False
    print("Access denied because the requested dataset is restricted.")


