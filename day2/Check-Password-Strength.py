import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1
    
    if score == 5: return "Very Strong"
    elif score >= 3: return "Moderate"
    else: return "Weak"

pwd = input("Enter password to check: ")
print(f"Password strength: {check_password_strength(pwd)}")
