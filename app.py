from tkinter import *
from tkinter import messagebox


def char_count():
    """Count the number of characters in the input text and display the count."""
    text = text_entry.get("1.0", END)
    # Subtracting 1 to exclude the newline character added by Text widget
    count = len(text) - 1
    char_count_label.config(text=f"Character Count: {count}")


def clear_text():
    """Clear the input text and reset the character count."""
    text_entry.delete("1.0", END)
    char_count_label.config(text="Character Count: 0")


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
count_button.pack(side=LEFT, padx=80)

clear_button = Button(app, text="Clear", font=('aria', 13), width=11, borderwidth=2, relief=GROOVE, command=clear_text)
clear_button.pack(side=LEFT)

app.mainloop()
