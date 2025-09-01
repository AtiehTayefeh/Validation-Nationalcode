
import sys

def validate_iranian_national_id(national_id):
    if not national_id.isdigit() or len(national_id) != 10:
        return False

    control_digit = int(national_id[9])
    sum_of_digits = 0
    for i in range(9):
        sum_of_digits += int(national_id[i]) * (10 - i)

    calculated_control_digit = sum_of_digits % 11

    if calculated_control_digit > 1:
        calculated_control_digit = 11 - calculated_control_digit

    return str(calculated_control_digit) == national_id[9]

# Simulate receiving the national ID as a command-line argument
# In a real scenario, you might get this from an API request body or query parameter.
# Here, we'll hardcode it for demonstration purposes, mimicking a call.
national_id_to_validate = "2093664402"

if validate_iranian_national_id(national_id_to_validate):
    print(f"کد ملی {national_id_to_validate} معتبر است.")
else:
    print(f"کد ملی {national_id_to_validate} نامعتبر است.")
