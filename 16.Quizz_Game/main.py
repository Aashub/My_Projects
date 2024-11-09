from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain



question_bank = []

for index, item in enumerate(question_data):

     question_text = question_data[index]["question"]
     question_answer = question_data[index]["correct_answer"]

     new_question = Question(question_text, question_answer)
     question_bank.append(new_question)


quiz = QuizzBrain(question_bank)
should_continue = True

while quiz.still_has_question():

     quiz.next_question()

print(f"You compeleted the Quizz.\n Your final score was: {quiz.current_score}/{quiz.question_number}")
