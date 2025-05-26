from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

from data import question_data

question_bank = []
for question in question_data:
    question_text = question["question"]
    correct_answer = question["correct_answer"]
    new_question = Question(question_text, correct_answer)
    question_bank.append(new_question)


quizz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quizz)
