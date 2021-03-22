from data import question_data
from question_model import Question
from quiz_brain import QUizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))

print(question_bank)

quiz = QUizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
print(f"YOur total score is {quiz.score}")