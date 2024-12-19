import tkinter as tk
from tkinter import messagebox
import sys
import os
import re
from decrypt import decrypt_trithemius

# Function to process input and display the decrypted result
def process_and_display():
    input_text = text_input.get("1.0", "end-1c")  # Get the text from input field
    if not input_text.strip():
        messagebox.showwarning("Warning", "The input field is empty!")
        return

    try:
        decrypted_text = decrypt_trithemius(input_text)
        output_text.delete("1.0", "end")  # Clear previous output
        output_text.insert("1.0", decrypted_text)  # Insert the decrypted result
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    global text_input, output_text

    # Create the main window
    root = tk.Tk()
    root.title("Trithemius Cipher Decryption")
    root.geometry("600x400")  # Set the window size

    # Title Label
    tk.Label(root, text="Trithemius Cipher Decryption", font=("Arial", 16)).pack(pady=10)

    # Input Text Field
    tk.Label(root, text="Enter Encrypted Text:", font=("Arial", 12)).pack(anchor="w", padx=10)
    text_input = tk.Text(root, wrap="word", height=8, width=70)
    text_input.pack(pady=5)

    # Decrypt Button
    decrypt_button = tk.Button(root, text="Decrypt Text", command=process_and_display, bg="lightblue", font=("Arial", 12))
    decrypt_button.pack(pady=10)

    # Output Text Field
    tk.Label(root, text="Decrypted Text:", font=("Arial", 12)).pack(anchor="w", padx=10)
    output_text = tk.Text(root, wrap="word", height=8, width=70, bg="#f0f0f0")
    output_text.pack(pady=5)

    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()