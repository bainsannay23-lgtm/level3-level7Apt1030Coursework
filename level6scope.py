def check_access(role):
    if role != "Doctor":
        raise PermissionError("Access Denied: Only Doctors can view patient records.")
    print("Access Granted.")

try:
    check_access("Nurse")
except PermissionError as e:
    print(e)

def scope_test():
    secure_data = "Patient History" 

print(secure_data) # This will raise a NameError since secure_data is not defined in this scope.