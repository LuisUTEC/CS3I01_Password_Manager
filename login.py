import tkinter as tk
import os
import app
import hashlib
import json
import secrets

def login():

    master_password = password_entry.get()

    if os.path.exists('passwords.json') and os.path.getsize('passwords.json') != 0:
        with open("passwords.json", "r") as file:
            json_str = file.read()
        data = json.loads(json_str)
        salt = data['main']['username']
        hashed = data['main']['password']
        if hashlib.shake_128(str(master_password + salt).encode('utf-8')).hexdigest(16) == hashed:
            login_window.destroy()
            app.open_password_manager(master_password)
            
        else:
            login_result_label.config(text="Invalid password")

    else:
        file = open("passwords.json", "w")
        passwords = {}
        salt = secrets.token_hex(8)
        hashed = hashlib.shake_128(str(master_password + salt).encode('utf-8')).hexdigest(16)
        passwords['main'] = {'username': salt, 'password': hashed}
        json_str = json.dumps(passwords)
        file.write(json_str)
        file.close()
        login_window.destroy()
        app.open_password_manager(master_password)

def on_enter(event):
    login_result_label.config(text="Hovering over the label")

def on_leave(event):
    login_result_label.config(text="Not hovering over the label")



login_window = tk.Tk()
login_window.title("Login")

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()

login_result_label = tk.Label(login_window, text="")
login_result_label.pack()

login_result_label.bind("<Enter>", on_enter)
login_result_label.bind("<Leave>", on_leave)



login_window.mainloop()
