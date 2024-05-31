import gnupg
import sys

def decrypt_message(encrypted_message, private_key, passphrase):
    # Création d'une instance de GPG
    gpg = gnupg.GPG()

    # Import de la clé privée
    import_result = gpg.import_keys(private_key)
    key_fingerprint = import_result.results[0]['fingerprint']

    # Déchiffrement du message
    decrypted_data = gpg.decrypt(encrypted_message, passphrase=passphrase)

    return decrypted_data.data

if __name__ == "__main__":

    # public.key on argv
    with open(sys.argv[1], "r") as file:
        private_key = file.read()
    
    with open(sys.argv[2], "r") as file:
        encrypted_message = file.read()

    print("Enter passphrase for decrypt: ")
    passphrase = input()

    decrypted_message = decrypt_message(encrypted_message, private_key, passphrase)

    print("Message decrypt: ")
    print(decrypted_message)


