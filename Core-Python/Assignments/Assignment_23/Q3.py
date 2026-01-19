import tkinter as tk

def calculate(op):
    a = float(num1.get())
    b = float(num2.get())

    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        res = a / b

    result.config(text=f"Result: {res}")

root = tk.Tk()
root.title("Calculator")

num1 = tk.Entry(root)
num2 = tk.Entry(root)

num1.grid(row=0, column=1)
num2.grid(row=1, column=1)

tk.Label(root, text="Number 1").grid(row=0, column=0)
tk.Label(root, text="Number 2").grid(row=1, column=0)

tk.Button(root, text="+", command=lambda: calculate('+')).grid(row=2, column=0)
tk.Button(root, text="-", command=lambda: calculate('-')).grid(row=2, column=1)
tk.Button(root, text="*", command=lambda: calculate('*')).grid(row=3, column=0)
tk.Button(root, text="/", command=lambda: calculate('/')).grid(row=3, column=1)

result = tk.Label(root, text="Result:")
result.grid(row=4, column=1)

root.mainloop()
