from exp import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)
while quiz.still_has_qns():
    quiz.next_question()
print(f'your final score : {quiz.score}/{quiz.question_no}')
