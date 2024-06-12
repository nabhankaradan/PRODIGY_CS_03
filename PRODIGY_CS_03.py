import re

def assess_password_strength(password):
    scores = [
        len(password) >= 8,
        re.search(r"[A-Z]", password),
        re.search(r"[a-z]", password),
        re.search(r"\d", password),
        re.search(r"[!@#$%^&*()_+=\-[\]{};:'\"|,.<>?\\]", password)
    ]
    
    total_score = sum(bool(criterion) for criterion in scores)

    if total_score <= 2:
        strength = "Weak"
    elif total_score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    feedback = (
        f"Length: {'Good' if scores[0] else 'Poor'}\n"
        f"Uppercase: {'Good' if scores[1] else 'Poor'}\n"
        f"Lowercase: {'Good' if scores[2] else 'Poor'}\n"
        f"Digits: {'Good' if scores[3] else 'Poor'}\n"
        f"Special Characters: {'Good' if scores[4] else 'Poor'}\n"
    )

    return strength, feedback

def main():
    password = input("Enter your password: ")

    strength, feedback = assess_password_strength(password)

    print(f"Password Strength: {strength}")
    print("Feedback:")
    print(feedback)

if __name__ == "__main__":
    main()
