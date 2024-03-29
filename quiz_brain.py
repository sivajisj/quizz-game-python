class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def check_the_answer(self,answer,crct_ans):
        if answer.lower() == crct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's a wrong")
        print(f"The correct answer was: {crct_ans}. ")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")




    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        correct_answer = current_question.answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_the_answer(user_answer,correct_answer)
