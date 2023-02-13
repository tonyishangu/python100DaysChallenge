from query_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = Quiz(question_bank)
while quiz.still_has_question:
    quiz.next_question()