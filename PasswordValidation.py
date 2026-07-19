def password_strength(password):
    if len(password) < 10:
        return "Bad"

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    score = sum([has_lower, has_upper, has_digit, has_special])

    if score >= 3:
        return "Best"
    elif score >= 2:
        return "Good"
    else:
        return "Bad"


password = input("Enter your password: ")
strength = password_strength(password)
print(f"Password strength: {strength}")
