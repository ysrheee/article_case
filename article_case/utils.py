import random
import string


def generate_key(n):
    KEY_SOURCE = string.ascii_letters + string.digits
    return ''.join(random.choice(KEY_SOURCE) for _ in range(n))
