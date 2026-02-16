from action import multi_layer, solve_multi

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