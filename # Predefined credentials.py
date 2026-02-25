# Predefined credentials
correct_username = "admin"
correct_password = "12345"

# Read input
username = input()
password = input()

# Validate
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")