import ciphers
import random

cipher_database = {
# didn't put parentheses to prevent the functions from being executed, they're references atm
    "atbash": {
        "id": "!H",
        "encrypt": ciphers.atbash_encryption,
        "decrypt": ciphers.atbash_decryption,
    },
    "affine": {
        "id": "/E",
        "encrypt": ciphers.affine_encryption,
        "decrypt": ciphers.affine_decryption,
    },
    "vigenere": {
        "id": "^V",
        "encrypt": ciphers.vigenere_en_default,
        "decrypt": ciphers.vigenere_de_default,
    },
    "rail_fence": {
        "id": "rF",
        "encrypt": ciphers.railfence_en_default,
        "decrypt": ciphers.railfence_de_default,
    },
    "polybius_square": {
        "id": "SP",
        "encrypt": ciphers.polybius_en_default,
        "decrypt": ciphers.polybius_de_default,
    }
}

# to fasten the process up, it matches the information using IDs
id_to_cipher = {data["id"]: data for data in cipher_database.values()}

def layer_ciphers(text):
    choice = random.choice(list(cipher_database.keys())) # keys for the names of the algorithms (KEYS: VALUES)
    cipher_id = cipher_database[choice]["id"]
    cipher_encrypt = cipher_database[choice]["encrypt"]
    return cipher_id + cipher_encrypt(text)

# this reads first two characters and decrypts the rest depending on the ID
def decrypt_layer(text):
    cipher_id = text[:2]
    encrypted_text = text[2:]
    cipher_data = id_to_cipher[cipher_id]
    decrypt_func = cipher_data["decrypt"]
    return decrypt_func(encrypted_text)


def multi_layer(text, layers = 5): # determine the layer number here
    result = text
    for i in range(layers):
        result = layer_ciphers(result)
    return result

def solve_multi(text, layers = 5): # repeat the layer number
    result = text
    for i in range(layers):
        result = decrypt_layer(result)
    return result