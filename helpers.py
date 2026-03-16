import random
import string

def gen_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(6))
    return password
def gen_email():
    return f"julia_pozdnyakova_41{random.randint(100, 999)}@gmail.com"

def gen_name():
    return "Julia"