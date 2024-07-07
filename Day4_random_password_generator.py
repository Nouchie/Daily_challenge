import random
import string

def generate_password(length=8, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    char_pool = ''
    
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    
    if not char_pool:
        raise ValueError("At least one character set must be selected")
    
    return ''.join(random.choice(char_pool) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired length of the password: "))
    
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
