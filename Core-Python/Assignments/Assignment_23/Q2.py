import tkinter as tk

rates = {
    "INR": 1,
    "USD": 0.012,
    "EUR": 0.011
}

def convert():
    amount = float(entry_amount.get())
    from_cur = from_currency.get()
    to_cur = to_currency.get()
    result = amount * rates[to_cur] / rates[from_cur]
    result_label.config(text=f"Converted Amount: {result:.2f}")

root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount").grid(row=0, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

from_currency = tk.StringVar(value="INR")
to_currency = tk.StringVar(value="USD")

tk.OptionMenu(root, from_currency, *rates.keys()).grid(row=1, column=0)
tk.OptionMenu(root, to_currency, *rates.keys()).grid(row=1, column=1)

tk.Button(root, text="Convert", command=convert).grid(row=2, column=1)

result_label = tk.Label(root, text="Converted Amount:")
result_label.grid(row=3, column=1)

root.mainloop()
