import tkinter as tk
from tkinter import messagebox

questions = [
    ("Python is ___ language?", ["High Level", "Low Level", "Machine"], "High Level"),
    ("Which keyword is used for function?", ["def", "fun", "function"], "def"),
    ("Which symbol is used for comments?", ["//", "#", "/*"], "#")
]

index = 0
score = 0

def check_answer(option):
    global index, score

    if option == questions[index][2]:
        score += 1
        messagebox.showinfo("Correct", "Correct Answer!")
    else:
        messagebox.showerror("Wrong", "Wrong Answer!")

    index += 1
    if index < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Finished", f"Score: {score}/{len(questions)}")
        root.destroy()

def load_question():
    q_label.config(text=questions[index][0])
    for i in range(3):
        buttons[i].config(text=questions[index][1][i])

root = tk.Tk()
root.title("Quiz Game")

q_label = tk.Label(root, text="")
q_label.pack()

buttons = []
for i in range(3):
    btn = tk.Button(root, command=lambda i=i: check_answer(buttons[i]["text"]))
    btn.pack()
    buttons.append(btn)

load_question()
root.mainloop()
