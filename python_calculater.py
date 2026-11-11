import tkinter as tk
import math

# Main Window
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("480x680")
root.minsize(420, 600)
root.configure(bg="#172033")

# Clear History Function (Defined first so buttons can reference it)
def clear_history():
    history_box.delete(0, tk.END)

# Button Click Function
def button_click(value):
    if value == "AC":
        display.delete(0, tk.END)

    elif value == "⌫":
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current[:-1])

    elif value == "π":
        display.insert(tk.END, str(math.pi))

    elif value == "x²":
        display.insert(tk.END, "**2")

    elif value == "xʸ":
        display.insert(tk.END, "**")

    elif value in ["sin", "cos", "tan", "log", "ln", "√"]:
        try:
            number = float(display.get())

            if value == "sin":
                result = math.sin(math.radians(number))
            elif value == "cos":
                result = math.cos(math.radians(number))
            elif value == "tan":
                result = math.tan(math.radians(number))
            elif value == "log":
                result = math.log10(number)
            elif value == "ln":
                result = math.log(number)
            else:
                result = math.sqrt(number)

            display.delete(0, tk.END)
            display.insert(0, str(result))

        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
            
    elif value == "=":
        try:
            expression = display.get()
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            history_box.insert(
                tk.END,
                f"{expression} = {result}"
            )
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    else:
        display.insert(tk.END, value)


# Calculator Display
display = tk.Entry(
    root,
    font=("Arial", 28, "bold"),
    bg="#1E293B",
    fg="#38BDF8",
    insertbackground="white",
    justify="right",
    bd=0,
    relief="flat"
)
display.pack(fill="x", padx=10, pady=20)

# History Section
history_label = tk.Label(
    root,
    text="Calculation History",
    font=("Arial", 12, "bold"),
    bg="#172033",
    fg="white"
)
history_label.pack(pady=5)

history_box = tk.Listbox(
    root,
    height=5,
    font=("Arial", 11),
    bg="#263449",
    fg="white"
)
history_box.pack(fill="x", padx=10, pady=5)

clear_history_btn = tk.Button(
    root,
    text="Clear History",
    font=("Arial", 11, "bold"),
    bg="#DC2626",
    fg="white",
    activebackground="#991B1B",
    relief="flat",
    cursor="hand2",
    command=clear_history
)
clear_history_btn.pack(pady=5)

# Calculator Main Heading
heading = tk.Label(
    root,
    text="SCIENTIFIC CALCULATOR",
    font=("Arial", 16, "bold"),
    bg="#172033",
    fg="white"
)
heading.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root, bg="#0F172A")
button_frame.pack(padx=10, pady=10, expand=True, fill="both")

# Configure grid weights for responsive resizing
for i in range(7):
    button_frame.rowconfigure(i, weight=1)
for j in range(4):
    button_frame.columnconfigure(j, weight=1)

# Button Names
buttons = [
    ["sin", "cos", "tan", "π"],
    ["log", "ln", "x²", "xʸ"],
    ["AC", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

# Button Creation
for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text == "AC":
            bg_color = "#DC2626"
        elif text == "=":
            bg_color = "#16A34A"
        elif text in ["+", "-", "*", "/", "%", "⌫"]:
            bg_color = "#2563EB"
        elif text in ["sin", "cos", "tan", "π", "log", "ln", "x²", "xʸ", "√"]:
            bg_color = "#7C3AED"
        else:
            bg_color = "#334155"

        btn = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 15, "bold"),
            bg=bg_color,
            fg="white",
            activebackground="#475569",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=lambda v=text: button_click(v)
        )

        btn.grid(
            row=r,
            column=c,
            padx=3,
            pady=3,
            sticky="nsew"
        )

# Keyboard Support
def keyboard_input(event):
    key = event.char
    if key in "0123456789.+-*/%":
        button_click(key)
    elif event.keysym == "Return":
        button_click("=")
    elif event.keysym == "BackSpace":
        button_click("⌫")
    elif event.keysym == "Escape":
        button_click("AC")

root.bind("<Key>", keyboard_input)

root.mainloop()