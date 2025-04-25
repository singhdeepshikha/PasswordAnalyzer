import tkinter as tk
from tkinter import ttk
import re

# Password analysis function
def analyze_password(password):
    suggestions = []
    score = 0

    # Length check
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    else:
        score += 1

    # Uppercase check
    if not re.search(r'[A-Z]', password):
        suggestions.append("Include at least one uppercase letter.")
    else:
        score += 1

    # Lowercase check
    if not re.search(r'[a-z]', password):
        suggestions.append("Include at least one lowercase letter.")
    else:
        score += 1

    # Digit check
    if not re.search(r'\d', password):
        suggestions.append("Include at least one number.")
    else:
        score += 1

    # Special character check
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include at least one special character.")
    else:
        score += 1

    # Common patterns
    common_patterns = ['123', 'password', 'abc', 'qwerty']
    if any(pattern in password.lower() for pattern in common_patterns):
        suggestions.append("Avoid common patterns like '123', 'password', etc.")

    # Final strength label
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score == 3 or score == 4:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, suggestions, color

# Toggle password visibility
def toggle_password():
    if entry_password.cget('show') == '':
        entry_password.config(show='*')
        btn_toggle.config(text='Show')
    else:
        entry_password.config(show='')
        btn_toggle.config(text='Hide')

# GUI logic
def evaluate_password():
    password = entry_password.get()
    strength, suggestions, color = analyze_password(password)

    label_result.config(text=f"Strength: {strength}", fg=color)

    text_suggestions.delete(1.0, tk.END)
    if suggestions:
        for suggestion in suggestions:
            text_suggestions.insert(tk.END, f"- {suggestion}\n")
    else:
        text_suggestions.insert(tk.END, "Great password! ✅")

# Create GUI window
root = tk.Tk()
root.title("Password Analyzer")
root.geometry("400x400")
root.config(bg="white")

# Title label
label_title = tk.Label(root, text="Password Analyzer", font=("Arial", 16, "bold"), bg="white", fg="#A63F00")
label_title.pack(pady=10)

# Password entry
entry_password = tk.Entry(root, width=30, show='*', font=("Arial", 12))
entry_password.pack(pady=10)

# Show/Hide button
btn_toggle = tk.Button(root, text="Show", command=toggle_password)
btn_toggle.pack()

# Analyze button
btn_analyze = tk.Button(root, text="Analyze Password", command=evaluate_password, bg="#FF8C42", fg="white", font=("Arial", 12, "bold"))
btn_analyze.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 14), bg="white")
label_result.pack(pady=10)

# Suggestions box
text_suggestions = tk.Text(root, height=8, width=45, font=("Arial", 10), wrap=tk.WORD, bg="#FFF3E0")
text_suggestions.pack(pady=10)

# Run GUI
root.mainloop()
