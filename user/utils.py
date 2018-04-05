import hashlib


def password_to_md5(password_raw):
    process = hashlib.md5()
    process.update(b'timesprindo')
    if not isinstance(password_raw, bytes):
        password_raw = bytes(password_raw, 'utf-8')
    process.update(password_raw)
    result = process.hexdigest()
    return result
