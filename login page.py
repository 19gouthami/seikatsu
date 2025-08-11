import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")

# Function to handle forgot password
def forgot_password():
    messagebox.showinfo("Forgot Password", "Password recovery link sent to your email.")

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.resizable(False, False)

# PYQ label in top-right corner
pyq_label = tk.Label(root, text="PYQ", font=("Arial", 10), fg="gray")
pyq_label.place(x=370, y=10)

# Username label and entry
tk.Label(root, text="Username:", font=("Arial", 12)).place(x=50, y=80)
username_entry = tk.Entry(root, width=30)
username_entry.place(x=150, y=80)

# Password label and entry
tk.Label(root, text="Password:", font=("Arial", 12)).place(x=50, y=120)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.place(x=150, y=120)

# Login button
login_button = tk.Button(root, text="Login", command=login, width=10, bg="blue", fg="white")
login_button.place(x=160, y=160)

# Forgot password link
forgot_button = tk.Button(root, text="Forgot Password?", command=forgot_password, fg="blue", bg="white", bd=0)
forgot_button.place(x=150, y=200)

# Run the app
root.mainloop()
