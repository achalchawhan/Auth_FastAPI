def signinEntity(item) -> dict:
    return {
        "email": item["email"],
        "password": item["password"],
        "important": item["important"],
    }

def signinsEntity(items) -> list:
    return [signinEntity(item) for item in items]


def signupEntity(item) -> dict:
    return {
        "firstName": item["firstName"],
        "lastName": item["lastName"],
        "phone": item["phone"],  # Update to match the form name
        "email1": item["email1"],
        "password1": item["password1"],
        "confirm_password": item["confirm_password"],
    }

def signupsEntity(items) -> list:
    return [signupEntity(item) for item in items]
