from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(plain_password: str) -> str:
    """
    Convert a plain password into a one-way hash string.

    This is what you will store in the users.password_hash column (field).
    """
    return generate_password_hash(plain_password)


def verify_password(stored_hash: str, candidate_password: str) -> bool:
    """
    Check if the candidate_password is correct for this stored hash.

    stored_hash -> value from users.password_hash (text column)
    candidate_password -> password the user just typed
    """
    return check_password_hash(stored_hash, candidate_password)