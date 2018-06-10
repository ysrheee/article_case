import hashlib

from article_case.utils import generate_key
from user.models import Profile


def password_to_md5(password_raw):
    process = hashlib.md5()
    process.update(b'timesprindo')
    if not isinstance(password_raw, bytes):
        password_raw = bytes(password_raw, 'utf-8')
    process.update(password_raw)
    result = process.hexdigest()
    return result


def authorize_user(user: Profile) -> str:
    auth = Profile.objects.filter(user=user)
    if not auth:
        key = generate_key(64)
        auth = Profile.objects.create(user=user, key=key)
    else:
        auth = auth.first()
    return auth.key
