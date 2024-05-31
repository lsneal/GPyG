import gnupg
import sys 

def encrypt_message(message, public_key):
    gpg = gnupg.GPG()

    import_result = gpg.import_keys(public_key)
    key_fingerprint = import_result.results[0]['fingerprint']

    encrypted_data = gpg.encrypt(message, key_fingerprint)

    return encrypted_data

if __name__ == "__main__":

    # public.key on argv
    with open(sys.argv[1], "r") as fichier:
        public_key = fichier.read()

    print("Enter message: ") 
    message = input()

    encrypted_data = encrypt_message(message, public_key)

    with open("message.gpg", 'w') as file:
        file.write(str(encrypted_data))

