class Level:
    def __init__(self):
        self.questions_left = 0
        pass
    def get_question(self):
        raise NotImplementedError( "Should have implemented this" )
    def is_correct(self, answer):
        raise NotImplementedError( "Should have implemented this" )

class CountingLevel(Level):
    def __init__(self):
        self.questions_left = 20
        self.question = None
        pass
    """
    Returns a new question to ask
    """
    def get_question(self):
        self.questions_left = self.questions_left - 1
        self.answer = random_number() # Number of objects
        # Return in a way for the view to parse and display animals/objects
        self.question = "counting: " + str(self.answer)
        return self.question
    def random_number(self):
        return randint(0,10)
    def is_correct(self, answer):
        try:
            given_answer = int(answer)
        except ValError:
            return False
        return given_answer == self.answer

class AdditionLevel(Level):
    def __init__(self):
        self.questions_left = 20
        pass
    """
    Returns a new question to ask
    """
    def get_question(self):
        self.questions_left = self.questions_left - 1
    def is_correct(self, answer):
        # Returns whether the given answer is correct or not
        pass
