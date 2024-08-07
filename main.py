from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Study Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
right = PhotoImage(file="C:/Users/pnatl/Documents/Coding/100 Days of Python/Flashcard Project/images/right.png")
left = PhotoImage(file="C:/Users/pnatl/Documents/Coding/100 Days of Python/Flashcard Project/images/wrong.png")
front_card = PhotoImage(file="C:/Users/pnatl/Documents/Coding/100 Days of Python/Flashcard Project/images/card_front.png")
back_card = PhotoImage(file="C:/Users/pnatl/Documents/Coding/100 Days of Python/Flashcard Project/images/card_back.png")

# Flashcard
canvas = Canvas(height=800, width=526)
canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.create_text(text="Mandarin", font=("Arial", 40, "italic"), bg="white", anchor="center")

# Buttons
right_button = Button(image=right, highlightthickness=0)
right_button.grid(column=1, row=1)
left_button = Button(image=left, highlightthickness=0)
left_button.grid(column=0, row=1)

# Labels
source_language = Label()
source_language.place(x=400, y=150, anchor="w")
translate_language = Label(text="English", font=("Arial", 60, "bold"), bg="white", anchor="center")
translate_language.place(x=400, y=263, anchor="w")

window.mainloop()
