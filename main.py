from tkinter import *
import random
import csv
import pandas
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/Translate Flashcards Capstone - Sheet1.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Mandarin")
    canvas.itemconfig(card_word, text=current_card["Chinese"])


window = Tk()
window.title("Study Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
right = PhotoImage(file="C:/Users/snatl/Documents/Coding/100 Days of Python/Flashcard Project/images/right.png")
wrong = PhotoImage(file="C:/Users/snatl/Documents/Coding/100 Days of Python/Flashcard Project/images/wrong.png")
front_card = PhotoImage(file="C:/Users/snatl/Documents/Coding/100 Days of Python/Flashcard Project/images/card_front.png")
back_card = PhotoImage(file="C:/Users/snatl/Documents/Coding/100 Days of Python/Flashcard Project/images/card_back.png")

# Flashcard
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=front_card)

card_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Buttons
right_button = Button(image=right, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()



window.mainloop()
