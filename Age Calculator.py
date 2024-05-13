import tkinter as tk

def calculate_age():
    # Retrieve the birth year from the entry widget
    birth_year = int(entry_birth_year.get())
    
    # Calculate the age
    age = 2024 - birth_year
    
    # Display the age in the label
    label_display.config(text="You are " + str(age) + " years old")

# Create the main window
window = tk.Tk()
window.title("Age Calculator")

# Create a label for instructions
label_instructions = tk.Label(window, text="Enter your birth year:")
label_instructions.pack()

# Create an entry widget for user input
entry_birth_year = tk.Entry(window)
entry_birth_year.pack()

# Create a button to trigger the action
button_submit = tk.Button(window, text="Calculate Age", command=calculate_age)
button_submit.pack()

# Create a label to display the calculated age
label_display = tk.Label(window, text="")
label_display.pack()

# Start the event loop
window.mainloop()
