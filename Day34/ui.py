from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.scorelabel = Label(text='Score:0', fg='white', bg=THEME_COLOR)
        self.scorelabel.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280,
            text='question ', 
            fill=THEME_COLOR,
            font=('Cursive', 24, 'italic')
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=true_img, highlightthickness=0)
        self.true_btn.grid(column=0, row=2)
        false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=false_img, highlightthickness=0)
        self.false_btn.grid(column=1,row=2,)

        self.get_next_question()

        self.window.mainloop()

        def get_next_question(self):
            q_text = self.quiz.next_question
            self.canvas.itemconfig(self.question_text, text=q_text)