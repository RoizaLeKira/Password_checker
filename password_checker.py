import re

def check_password_strength(password):
    """Evaluates the strength of a password based on specific criteria."""
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters."
    if not re.search(r"[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Weak: Password must contain at least one digit."
    if not re.search(r"[@$!%*?&]", password):
        return "Weak: Password must contain at least one special character (@$!%*?&)."
    return "Strong password!"

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)
