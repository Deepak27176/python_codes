class QuizBrain:

    def __init__(self,q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score=0

    def still_has_qns(self):
        return self.question_no < len(self.question_list)


    def next_question(self):
        current_qns = self.question_list[self.question_no]
        self.question_no += 1
        ans= input(f'Q.{self.question_no}:{current_qns.text} (True/False):')
        self.check_ans( ans, current_qns.answer,self.question_no)

    def check_ans(self,user_ans,correct_ans,Q_no):

        if user_ans == correct_ans:
            print('you got it right')
            self.score += 1


        else:
            print("you are wrong")
            print(f'the correct answer was : {correct_ans}')



