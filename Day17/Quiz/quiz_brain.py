# TODO: asking the question
# TODO: Checking if the answer is correct
# TODO: Check if quiz is still ongoing


class Quiz:

    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list

    def still_has_question(self):
        length = len(self.q_list)
        return self.q_num < length
            

    def next_question(self):
        current_q = self.q_list[self.q_num]
        self.q_num += 1
        input(f'Q.{self.q_num}: {current_q.text} (True or False): \n')