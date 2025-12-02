import tkinter as tk
from tkinter import messagebox
from helper import analyze_password
import random
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x520")
root.resizable(False, False)
root.config(bg="#000000")  
def get_labels(score):
    labels = {0: "Very Weak", 1: "Weak", 2: "Fair", 3: "Strong", 4: "Very Strong"}
    return labels.get(score, "Unknown")
show_password = False
def toggle_password():
    global show_password
    if show_password:
        password_entry.config(show="*")
        eye_button.config(text="👁")
        show_password = False
    else:
        password_entry.config(show="")
        eye_button.config(text="🙈")
        show_password = True
def insert_coloured_suggestions(issues):
    suggestions_text.delete(1.0,tk.END)
    for line in issues:
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        suggestions_text.tag_configure(color,
            foreground=color,font=("Arial", 12, "bold"))
        suggestions_text.insert(tk.END, line + "\n", color)
def check_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return
    issues, score = analyze_password(password)
    label = get_labels(score)
    strength_label.config(text=f"Strength: {label} ({score}/4)", font=("Arial", 14, "bold"))
    suggestions_text.delete(1.0, tk.END)
    if issues:
        insert_coloured_suggestions(issues)
    else:
        suggestions_text.insert(tk.END, "No issues found!")
def live_update(event):
    check_password()
tk.Label(root, text="Enter Password:", fg="white", bg="#000000",
         font=("Arial", 12)).pack(pady=15)
password_frame = tk.Frame(root, bg="#000000")
password_frame.pack()
password_entry = tk.Entry(password_frame, width=30, show="*",bg="#1A1A1A", fg="white",insertbackground="white")              
password_entry.pack(side="left")
eye_button = tk.Button(password_frame, text="👁", command=toggle_password, bg="#333333", fg="white", activebackground="#666666")
eye_button.pack(side="left", padx=5)
password_entry.bind("<KeyRelease>",live_update)
check_button = tk.Button(root, text="Check Password",command=check_password,bg="#333333", fg="white",activebackground="#555555")                
check_button.pack(pady=10)
strength_label = tk.Label(root, text="Strength:", fg="white", bg="#000000")                       
strength_label.pack(pady=10)
tk.Label(root, text="Suggestions:", fg="white",bg="#000000").pack()      
suggestions_text = tk.Text(root, height=10, width=45,bg="#1A1A1A", fg="white", insertbackground="white")                        
suggestions_text.pack(pady=10)
root.mainloop()
