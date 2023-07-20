def v_p(password):
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    special_chars = "!@#$%^&*"
    if not any(char in special_chars for char in password):
        return False

    return True

password = "Str0ngp@ssword"
print(v_p(password))

password = "weakpass"
print(v_p(password))