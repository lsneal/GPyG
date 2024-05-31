import gnupg

def generate_pgp_keys():
    # instance GPG
    gpg = gnupg.GPG()
    
    print("Name: ")
    name_real = input()
    print("Email: ")
    name_email = input()
    print("Expiration format: 1 month = 1m | 1 year = 1y\n")
    print("Expiration: ")
    expire_date = input()
    print("Enter your passphrase for privatekey: ")
    passphrase = input()

    input_data = gpg.gen_key_input(
        key_type="RSA",
        key_length=2048,
        passphrase=passphrase,
        name_real=name_real,
        name_email=name_email,
        expire_date=expire_date
    )
    key = gpg.gen_key(input_data)

    private_key = gpg.export_keys(key.fingerprint, secret=True, passphrase=passphrase)
    public_key = gpg.export_keys(key.fingerprint)

    return private_key, public_key

if __name__ == "__main__":
    private_key, public_key = generate_pgp_keys()

    with open("private.key", 'w') as file:
        file.write(private_key)

    with open("public.key", 'w') as file:
        file.write(public_key)
