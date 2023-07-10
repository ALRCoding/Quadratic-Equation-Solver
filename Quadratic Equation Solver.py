from tkinter import *
from fractions import Fraction

# Create the main window
root = Tk()
root.title("Quadratic Equation Solver")

# Set the size of the window
root.geometry("400x400")

# Create a label for the equation
eqn_label = Label(root, text="ax² + bx + c = 0", font=("Arial", 18))
eqn_label.pack(pady=20)

# Create a frame to hold the input fields and labels
input_frame = Frame(root)
input_frame.pack(pady=20)

# Create labels for the input fields
a_label = Label(input_frame, text="a = ")
a_label.grid(row=0, column=0, padx=10)

b_label = Label(input_frame, text="b = ")
b_label.grid(row=1, column=0, padx=10)

c_label = Label(input_frame, text="c = ")
c_label.grid(row=2, column=0, padx=10)

# Create variables for the input fields
a_var = StringVar()
b_var = StringVar()
c_var = StringVar()

# Create entry fields for the variables
a_entry = Entry(input_frame, textvariable=a_var, font=("Arial", 14), width=5)
a_entry.grid(row=0, column=1)

b_entry = Entry(input_frame, textvariable=b_var, font=("Arial", 14), width=5)
b_entry.grid(row=1, column=1)

c_entry = Entry(input_frame, textvariable=c_var, font=("Arial", 14), width=5)
c_entry.grid(row=2, column=1)

# Create a function to solve the quadratic equation
def solve():
    a = Fraction(a_var.get())
    b = Fraction(b_var.get())
    c = Fraction(c_var.get())

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is negative
    if discriminant < 0:
        root_label.config(text="No real roots")
    else:
        # Calculate the two roots
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)

        # Show the roots
        root1_label.config(text=f"x = {root1}")
        root2_label.config(text=f"x = {root2}")

# Create a solve button
solve_button = Button(root, text="Solve", font=("Arial", 14), command=solve)
solve_button.pack(pady=10)

# Create labels to display the roots
root_label = Label(root, text="")
root_label.pack()

root1_label = Label(root, text="")
root1_label.pack()

root2_label = Label(root, text="")
root2_label.pack()

# Run the main loop
root.mainloop()
