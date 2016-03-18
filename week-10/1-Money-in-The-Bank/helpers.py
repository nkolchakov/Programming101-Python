import hashlib
import random


def generate_salt():
    rbits = random.getrandbits(256)
    m = hashlib.sha256()
    m.update(str(rbits).encode('utf-8'))

    return m.hexdigest()


def hash_password_salt_tuple(password, salt=None):
    m = hashlib.sha256()

    if salt is None:
        salt = generate_salt()

    concat = password + salt
    m.update(concat.encode('utf-8'))

    return (m.hexdigest(), salt)
