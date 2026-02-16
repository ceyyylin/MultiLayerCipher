# added wrappers to vigenere, rail fence and polybius.
# since atbash and affine don't have any keys, no need to add wrappers to them

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

# wrappers
def vigenere_en_default(text):
    return vigenere_encryption(text, "PiaMater")

def vigenere_de_default(text):
    return vigenere_decryption(text, "PiaMater")

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

# wrappers
def railfence_en_default(text):
    return railfence_encryption(text, 3)

def railfence_de_default(text):
    return railfence_decryption(text, 3)

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

# wrappers
def polybius_en_default(text):
    return polybius_encryption(text, row_key, col_key)

def polybius_de_default(text):
    return polybius_decryption(text, row_key, col_key)