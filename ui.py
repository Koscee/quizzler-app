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

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
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
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_clicked(self):
        self.give_feed_back(self.quiz.check_answer("True"))

    def false_clicked(self):
        self.give_feed_back(self.quiz.check_answer("False"))

    def give_feed_back(self, is_right):
        bkg_color = "#5BB780" if is_right else "#FF8086"
        self.canvas.config(bg=bkg_color)
        self.window.after(1000, self.get_next_question)
