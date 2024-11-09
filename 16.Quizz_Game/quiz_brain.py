

class QuizzBrain:

    def __init__(self, question_list):

        self.question_number  = 0
        self.current_score = 0
        self.question_list = question_list

    def still_has_question(self):

        if self.question_number < len(self.question_list):
            return  True
        else:
            return False

    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.current_score += 1
            print(f"you got it! ")

        else:
            print("Sorry that's wrong answer.")

        print(f"the correct answer is {correct_answer},")
        print(f"current_score is {self.current_score}/{self.question_number}")
        print("\n")





