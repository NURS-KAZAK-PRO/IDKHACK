import tkinter as tk
from tkinter import ttk, messagebox
import time

def start_prank():
    # Update the label and start the progress bar
    label.config(text="Bypassing Firewall...")
    progress['value'] = 0
    
    for i in range(1, 11):
        time.sleep(0.3) # Simulates loading time
        progress['value'] += 10
        root.update_idletasks()
    
    label.config(text="Accessing System Files...")
    time.sleep(1)
    
    # The final "Boom" message
    messagebox.showwarning("SYSTEM CRITICAL", "BOOM! System Bombing Initiated!")
    
    # The Reveal
    messagebox.showinfo("Pranked!", "Don't worry, it's fake. \nYou've been pranked! :P")
    root.destroy()

# Set up the main window
root = tk.Tk()
root.title("System Terminal v4.0")
root.geometry("400x200")

label = tk.Label(root, text="Click to Initialize Breach", font=("Courier", 12))
label.pack(pady=20)

# Progress bar to look like a "hacking" bar [##########]
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

btn = tk.Button(root, text="START HACK", command=start_prank, bg="red", fg="white")
btn.pack(pady=10)

root.mainloop()
