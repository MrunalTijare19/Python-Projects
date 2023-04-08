from num2words import num2words
import tkinter as tk
from tkinter import messagebox

def convert_number():
    number = entry.get()
    try:
        # Convert the input to integer
        number = int(number)
        
        # Check if the number is within the valid range
        if number < 0 or number > 999999999:
            raise ValueError("Number must be between 0 and 999,999,999")
        
        # Convert the number to words using num2words
        words = num2words(number).replace(",", "")
        
        # Update the label with the result
        label.config(text=f"Words: {words}")
    except ValueError as e:
        # Show error message if input is not a valid number
        messagebox.showerror("Error", str(e))
    except Exception as e:
        # Show generic error message for other exceptions
        messagebox.showerror("Error", "An error occurred: " + str(e))

# Create a tkinter window
root = tk.Tk()
root.title("Number to Words Converter")

# Create a label for input prompt
prompt = tk.Label(root, text="Enter a number (0-999,999,999):")
prompt.pack()

# Create an entry for number input
entry = tk.Entry(root)
entry.pack()

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_number)
convert_button.pack()

# Create a label to display the result
label = tk.Label(root, text="")
label.pack()

# Run the tkinter event loop
root.mainloop()
