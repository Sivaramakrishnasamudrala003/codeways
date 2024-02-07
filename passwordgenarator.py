import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length <= 0:
            raise ValueError("Length should be a positive integer.")
        
        generated_password = generate_password(password_length)
        print("Generated Password: ", generated_password)
    
    except ValueError as e:
        print("Error:", e)
if __name__ == "__main__":
    main()

