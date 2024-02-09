import random
import string

def generate_password(length=12, include_lowercase=True, include_uppercase=True, include_digits=True, include_special_chars=True):
    # Define character sets
    lowercase_chars = string.ascii_lowercase if include_lowercase else ''
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    digit_chars = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Ensure the password length is at least 4 characters and includes at least one character from each set
    length = max(4, length)
    password = (
        random.choice(lowercase_chars) +
        random.choice(uppercase_chars) +
        random.choice(digit_chars) +
        random.choice(special_chars) +
        ''.join(random.choice(all_chars) for _ in range(length - 4))
    )

    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

if __name__ == "__main__":
    # Example usage
    password = generate_password()
    print("Generated Password:", password)