from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {0}", bg=THEME_COLOR, fg="white", font=('Arial', 15))
        self.score_label.grid(row=0, column=1, sticky="nse")

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question Goes Here", fill=THEME_COLOR,
                                                     font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img_icon = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img_icon, border=0, highlightthickness=0, command=self.true_clicked)
        self.true_btn.grid(row=2, column=0)

        false_img_icon = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img_icon, border=0, highlightthickness=0, command=self.false_clicked)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_clicked(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def false_clicked(self):
        self.quiz.check_answer("False")
        self.get_next_question()
