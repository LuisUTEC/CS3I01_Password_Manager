import tkinter as tk
import json
import AES
import string
import random


def open_password_manager(key):
    print(key)
    password_manager = tk.Tk()
    password_manager.title("Password Manager")
    with open('passwords.json', 'r') as file:
        json_str = file.read()
    passwords = json.loads(json_str)

    def save_passwords():
        with open('passwords.json', 'w') as file:
            json.dump(passwords, file)

    def add_password():
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        if check_password(password) == True:
            website = AES.AES128Encryption(key,website,True)
            username = AES.AES128Encryption(key,username,True)
            password = AES.AES128Encryption(key,password,True)
            passwords[website] = {'username': username, 'password': password}
            save_passwords()
            result_label.config(text="Password added successfully.")
        else:
            error_text = "Password is weak, try using: " + str(generate_password())
            result_label.config(text= error_text)

    def get_password():
        website = website_entry.get()
        website = AES.AES128Encryption(key,website)
        if website in passwords:
            username = passwords[website]['username']
            print(username)
            username = AES.AES128Decryption(key,username)
            password = AES.AES128Decryption(key,passwords[website]['password'])
            result_label.config(text=f"Username: {username}\nPassword: {password}")
        else:
            result_label.config(text="Website not found in password manager.")

    def delete_password():
        website = website_entry.get()
        website = AES.AES128Encryption(key,website)
        if website in passwords:
            del passwords[website]
            result_label.config(text="Password deleted successfully.")
            save_passwords()
        else:
            result_label.config(text="Website not found in password manager.")

    def check_password(password: str):
        size = False
        upper = False
        lower = False
        special_char = False
        number = False
        common = True

        if len(password) > 10:
            size = True
        
        for i in password:
            if i.islower():
                lower = True
            elif i.isupper():
                upper = True
            elif i in string.punctuation:
                special_char = True
            elif i.isnumeric():
                number = True

        with open("diccionario.txt", "r") as file:
            for word in file:
                if word.strip() == password:
                    common = False
        if size == True and upper == True and lower == True and special_char == True and number == True and common == True:
            return True
        else:
            return False

    def generate_password():
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''
        
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        
        password += ''.join(random.choice(characters) for i in range(7))
        
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)
        
        if check_password(password):
            return password
        else:
            generate_password()

    def list_websites():
        websites = list(passwords.keys())[1:]
        for i in range(len(websites)):
            websites[i] = AES.AES128Decryption(key,websites[i])
        result_label.config(text="Websites:\n{}".format("\n".join(websites)))

    def exit_app():
        password_manager.destroy()
    
    website_label = tk.Label(password_manager, text="Website:")
    website_label.pack()
    website_entry = tk.Entry(password_manager)
    website_entry.pack()

    username_label = tk.Label(password_manager, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(password_manager)
    username_entry.pack()

    password_label = tk.Label(password_manager, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(password_manager, show="*")
    password_entry.pack()

    add_button = tk.Button(password_manager, text="Add Password", command=add_password)
    add_button.pack()

    get_button = tk.Button(password_manager, text="Get Password", command=get_password)
    get_button.pack()

    delete_button = tk.Button(password_manager, text="Delete Password", command=delete_password)
    delete_button.pack()

    list_button = tk.Button(password_manager, text="List Websites", command=list_websites)
    list_button.pack()

    result_label = tk.Label(password_manager, text="")
    result_label.pack()

    exit_button = tk.Button(password_manager, text="Exit", command=exit_app)
    exit_button.pack()


    password_manager.mainloop()

if __name__ == "__main__":
    open_password_manager("key")
