import hashlib

def make_password(password: str):
    return hashlib.sha512(password).hexdigest()
