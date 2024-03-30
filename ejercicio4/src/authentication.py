import bcrypt


def get_password_hash(password):
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf8'), hashed_password.encode('utf8'))