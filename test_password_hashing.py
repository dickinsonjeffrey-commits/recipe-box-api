from auth_utils import hash_password, verify_password


def main():
    # Use a fake password ONLY for testing
    plain_password = "test-password-123"

    # Create a hash (this is what would be stored in users.password_hash)
    stored_hash = hash_password(plain_password)

    print("Plain password:", plain_password)
    print("Stored hash:", stored_hash)

    # Now try verifying the correct password
    is_correct = verify_password(stored_hash, "test-password-123")

    # And an incorrect one
    is_incorrect = verify_password(stored_hash, "wrong-password")

    print("Correct password matches:", is_correct)
    print("Wrong password matches:", is_incorrect)


if __name__ == "__main__":
    main()