import re


def validate_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None

def validate_date(date_str):
    if date_str is None:
        return True

    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"

    if re.match(pattern, date_str):
        return True
    else:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return False
