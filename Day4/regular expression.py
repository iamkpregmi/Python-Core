import re

# Validate an Email Address
# email  = "user@example.com"
# pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'

# is_valid = re.match(pattern,email)
# if is_valid:
#     print("Email is Valid")
# else:
#     print("Email is not valid")


# # Extract all phone numbers from a message
# text = "Call me at 9876543210 or 9123456789"
# phones = re.findall(r'\b\d{10}\b', text)
# print(phones) # ['9876543210', '9123456789']


# # Replace all digits with *
# text = "My OTP is 123456"
# new_text = re.sub(r'\d', '*', text)
# print(new_text)  # My OTP is ******


# # Check password strength (at least 8 chars, one uppercase, one digit):
# password = "StrongPass1"
# pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'

# if re.match(pattern, password):
#     print("Strong Password")
# else:
#     print("Weak Password")

