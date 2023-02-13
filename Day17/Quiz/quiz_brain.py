# TODO: asking the question
# TODO: Checking if the answer is correct
# TODO: Check if quiz is still ongoing


class Quiz:

    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.q_num < len(self.q_list)

    def next_question(self):
        current_q = self.q_list[self.q_num]
        self.q_num += 1
        user_ans = input(f'Q.{self.q_num}: {current_q.text} (True or False): \n')
        self.check_answer(user_ans, current_q.answer)
      
    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print('Correct')
        else:
            print('Wrong')
            print(f'Correct Score is: {correct_ans}')
    
        print(f'Your Score is {self.score}/{self.q_num}')
        print('\n')