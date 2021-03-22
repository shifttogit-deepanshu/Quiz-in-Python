class QUizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}:{current_question.text} (True/False)?")
        self.check_answer(choice,current_question.answer)

    def check_answer(self,user_choice,correct_answer):
        if user_choice.lower() == correct_answer.lower():
            print("you are right!")
            self.score +=1
        else:
            print("You are wrong!")
        print(f"The correct answer was {correct_answer}")
        print(f"{self.score}/{self.question_number}")