import view
import model

class Controller:
    def __init__(self):
        self.view = view.View()
    """
    Call this method to start a new game starting at level 1
    """
    def start_new_game(self):
        self.level_num = 1
        self.start_game()
    """
    Call this method to start a new game at a certain level
    """
    def start_game_at_level(self, level):
        self.level_num = level
        self.start_game()
    """
    Call this method to start a game based on current level
    """        
    def start_game(self):
        self.score = 0
        if self.level_num < 3:
            self.level = model.CountingLevel()
        else:
            self.level = model.AdditionLevel()
        self.ask_new_question()
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
        self.ask_question()
    """
    Returns a boolean whether the given answer matches the level's answer or not
    """
    def verify_answer(self, answer):
        return self.level.is_correct(answer)
    """
    Callback for the view when an answer is given. Determines what to do with the given answer and how to proceed.
    """
    def handle_answer(self, answer):
        if self.verify_answer(answer):
            # Success, go to next level
            self.score = self.score + 3
            if (self.level.questions_left > 0) and (self.score < (3 * 15)):
                # Ask another question
                self.ask_new_question()
            else:
                # Answered all of the questions in the level, ask if want to go to next level
                if self.view.ask_next_level():
                    self.level_num = self.level_num + 1
                    self.start_game()
                else:
                    # User wants to stay on this level, so ask new questions
                    self.ask_new_question()  
        else:
            # Failed, try again with same question?
            self.ask_question()