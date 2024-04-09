from tkinter import *
from tkinter import messagebox


def char_count():
    text = text_entry.get("1.0", END)
    count = len(text) - 1
    char_count_label.config(text=f"Character Count: {count}")


app = Tk()
app.title("Character Counter")
app.geometry("500x440")
app.config(pady=10, padx=10)

app_label = Label(app, text="Character Counter", font=('nectar regular', 18, "bold"))
app_label.pack()

underline_label = Label(app, text="____________________", font=('nectar regular', 16))
underline_label.pack()

text_entry = Text(app, borderwidth=2, relief=GROOVE, width=40, height=13)
text_entry.pack(pady=10)

char_count_label = Label(app, font=('aria', 12), fg="#212121")
char_count_label.pack(pady=15)

count_button = Button(app, text="Count", font=('aria', 13), width=11, borderwidth=2, relief=GROOVE, command=char_count)
count_button.pack()

app.mainloop()