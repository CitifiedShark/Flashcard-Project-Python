from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Translate Flashcards Capstone - Sheet1.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card_right():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)

    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(card_title, text="Mandarin")
    canvas.itemconfig(card_word, text=current_card["Chinese"])
    canvas.itemconfig(card_title, fill="black")
    canvas.itemconfig(card_word, fill="black")

    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_title, fill="white")
    canvas.itemconfig(card_word, fill="white")

window = Tk()
window.title("Study Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Images
right = PhotoImage(file="C:/Users/pnatl/Documents/Coding/100 Days of Python/Flashcard Project/images/right.png")
wrong = PhotoImage(file="C:/Users/pnatl/Documents/Coding/100 Days of Python/Flashcard Project/images/wrong.png")
front_card = PhotoImage(file="C:/Users/pnatl/Documents/Coding/100 Days of Python/Flashcard Project/images/card_front.png")
back_card = PhotoImage(file="C:/Users/pnatl/Documents/Coding/100 Days of Python/Flashcard Project/images/card_back.png")

# Flashcard
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=front_card)

card_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Buttons
right_button = Button(image=right, highlightthickness=0, command=next_card_right)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()



window.mainloop()
