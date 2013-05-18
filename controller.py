class Controller:
    def __init__(self):
        pass

    """
    Call this method to start a new game starting at level 1
    """
    def start_new_game(self):
        self.level_num = 1
        self.score = 0
        self.start_game()
    """
    Call this method to start a game based on current level
    """        
    def start_game(self):
        if self.level_num < 3:
            self.level = CountingLevel()
        else:
            self.level = AdditionLevel()
        ask_new_question()
    """
    Asks the current question
    """
    def ask_question(self):
        self.view.display_question(self.question, self.handle_answer)
    """
    Asks a newly generated question
    """
    def ask_new_question(self):
        self.question = self.level.get_question()
        ask_question()
    """
    Returns a boolean whether the given answer matches the level's answer or not
    """
    def verify_answer(self, answer):
        return self.level.is_correct(answer)
    """
    Callback for the view when an answer is given. Determines what to do with the given answer and how to proceed.
    """
    def handle_answer(self, answer):
        if verify_answer(answer):
            # Success, go to next level
            self.score = self.score + 3
            if (self.level.question_left>0) and (self.score<(3*15)):
                # Ask another question
                ask_new_question()
            else:
                # Answered all of the questions in the level, ask if want to go to next level
                if self.view.ask_next_level():
                    self.level_num = self.level_num + 1
                    start_game()
                else:
                    #user wants to stay on this level, so ask new questions
                    ask_new_question()  
        else:
            # Failed, try again with same question?
            ask_question()
       
    """
    Keep track of the questions (numbers) has been asked, and how many times (no more than 2)
    """
    def asked_number(self):
        """
        if number exist:
            add 1 to count
        else:
            append (number,count) to lst, where count=1
        """
