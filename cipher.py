import random

# ATBASH
def atbash_encryption(text):
    result = ""
    for char in text:
        first_value = ord(char) - 32 # to skip binary
        final_value = 94 - first_value # to find the new value (94 total)
        new_char = chr(final_value + 32) # turn it back into ASCII
        result += new_char
    return result

def atbash_decryption(text):
    return atbash_encryption(text)

# AFFINE
def affine_encryption(text):
    result = ""
    for char in text:
        x = ord(char) - 32
        y = (47*x + 42) % 95 # a = 47, b = 42 -> could change the values later
        result += chr(y + 32)
    return result

def affine_decryption(text):
    result = ""
    # pow(number, -1, mod) gives the modular inverse
    a_inv = pow(47, -1, 95)
    for char in text:
        y = ord(char) - 32
        x = (a_inv * (y - 42)) % 95 # x = (a_inv * (y - b)) % 95
        result += chr(x + 32)
    return result

# VIGENERE
def vigenere_encryption(text, key):
    result = ""
    for i, char in enumerate(text): # gives every item an index
        input_val = ord(char) - 32
        key_char = key[i % len(key)] # the key repeats until there's nothing left
        key_val = ord(key_char) - 32
        total_val = (input_val + key_val) % 95 # mod to prevent from overflow
        result += chr(total_val + 32)
    return result

def vigenere_decryption(encrypted_text, key):
    result = ""
    # reverse operation of vigenere encryption (subtract key instead of adding)
    for i, char in enumerate(encrypted_text):
        encrypted_val = ord(char) - 32
        key_char = key[i % len(key)]
        key_val = ord(key_char) - 32
        real_val = (encrypted_val - key_val) % 95
        result += chr(real_val + 32)
    return result

# RAIL FENCE
def railfence_encryption(text, rail_num):
    if rail_num <= 1:
        return text
    rails = [""] * rail_num # creates a list like ["", "", ""]
    row = 0
    direction = 1 # 1 for down, -1 for up
    for char in text:
        rails[row] += char # adds the char to the current spot
        row += direction # move to the next row, didn't write a constant value so it change directions
        if row == 0 or row == rail_num - 1:
            direction *= -1 # multiply by -1 to change direction
    return "".join(rails) #combine all chars

def railfence_decryption(encrypted_text, rail_num):
    # create zigzags and give each char a value
    length = len(encrypted_text)
    pattern = []
    row = 0
    direction = 1
    for i in range(length):
        pattern.append(row)
        row += direction
        if row == 0 or row == rail_num - 1:
            direction *= -1
    # sort the values
    arranged = sorted(range(len(pattern)), key = lambda i: pattern[i]) # it sorts the values of indexes but gives the indexes as an output instead
    # create a list for the final position
    result = [""] * length
    # put the char to the correct places using the for loop like a coordinate of (i, pos)
    for i, pos in enumerate(arranged):
        result[pos] = encrypted_text[i]
    return "".join(result) # didn't just use result because it's in a list format, this line turns it back into string

# POLYBIUS SQUARE
row_key = "*p+Pzm^%2|"
col_key = "qE!?<>KCz3"
def polybius_encryption(text, row_key, col_key):
    # creates a 10x10 square, finds and prints the "coordinates" of each char
    chars = "".join([chr(i) for i in range(32, 127)]) # a list of ASCII chars
    result = ""
    for char in text:
        find_index = chars.index(char) # finds the arrangement (example: 33 for A and gives the output of 33)
        row = find_index // 10
        col = find_index % 10 # using mod to create an endless cycle
        result += row_key[row] + col_key[col] # writes the result together (example: row = 2, col = 6, result = +>)
    return result

def polybius_decryption(text, row_key, col_key):
    chars = "".join([chr(i) for i in range(32, 127)])
    result = ""
    for i in range(0, len(text), 2):
        row_index = row_key.index(text[i]) # # find row index in row_key
        col_index = col_key.index(text[i + 1]) # find column index in col_key
        index = row_index * 10 + col_index # find the ASCII value
        result += chars[index]
    return result


# a highly unpractical function
# picks a random cipher and attaches an ID
def layer_ciphers(text):
    choice = random.choice(["atbash", "affine", "vigenere", "rail_fence", "polybius_square"]) # added the list inside choices to avoid an extra list
    # determine all IDs here
    if choice == "atbash":
        return "!H" + atbash_encryption(text)
    elif choice == "affine":
        return "/E" + affine_encryption(text)
    elif choice == "vigenere":
        return "^V" + vigenere_encryption(text, "PiaMater") # determine the key here
    elif choice == "rail_fence":
        return "rF" + railfence_encryption(text, 3) # determine the rail number here
    elif choice == "polybius_square":
        return "SP" + polybius_encryption(text, row_key, col_key)


# this reads first two characters and decrypts the rest depending on the ID
def decrypt_layer(text):
    ID = text[:2]
    encrypted_part = text[2:]
    if ID == "!H":
        return atbash_decryption(encrypted_part)
    elif ID == "/E":
        return affine_decryption(encrypted_part)
    elif ID == "^V":
        return vigenere_decryption(encrypted_part, "PiaMater") # repeat the key
    elif ID == "rF":
        return railfence_decryption(encrypted_part, 3) # repeat the rail number
    elif ID == "SP":
        return polybius_decryption(encrypted_part, row_key, col_key)

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

def main():
    while True:
        print("\n[Main Menu]")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, 3) : ")
        print("-" * 30)
        if choice == "1":
            print("\n[Encryption]")
            text = input("Enter your text: ")
            encrypted_text = multi_layer(text)
            print("Encrypted text: ", encrypted_text)
            print("-" * 30)

        elif choice == "2":
            print("\n[Decryption]")
            text = input("Enter your text: ")
            decrypted_text = solve_multi(text)
            print("Decrypted text: ", decrypted_text)
            print("-" * 30)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter your choice 1, 2 or 3 ")

if __name__ == "__main__":
    main()