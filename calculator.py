import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

display_var = tk.StringVar(value="0")

def btn_click(char):
    current = display_var.get()
    if current == "0":
        display_var.set(char)
    else:
        display_var.set(current + char)

def btn_clear():
    display_var.set("0")

def btn_equal():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except:
        display_var.set("Error")

# Display
tk.Label(root, textvariable=display_var, font=("Arial", 24), bg="lightgray", height=2).pack(fill="both", padx=5, pady=5)

# Buttons frame
btns_frame = tk.Frame(root)
btns_frame.pack(padx=5, pady=5)

buttons = [
    ("C", 1, 0), ("%", 1, 1), ("/", 1, 2), ("*", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),
    (".", 5, 1)
]

for (text, row, col) in buttons:
    if text == "C":
        cmd = btn_clear
    elif text == "=":
        cmd = btn_equal
    else:
        cmd = lambda x=text: btn_click(x)

    tk.Button(
        btns_frame, text=text, width=8, height=2, font=("Arial", 14),
        bd=2, relief="ridge", command=cmd
    ).grid(row=row, column=col, padx=3, pady=3)

# Extra big "0" button
tk.Button(
    btns_frame, text="0", width=18, height=2, font=("Arial", 14),
    bd=2, relief="ridge", command=lambda: btn_click("0")
).grid(row=5, column=0, columnspan=2, padx=3, pady=3)

root.mainloop()