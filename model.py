from random import randint

class Level:
    def __init__(self):
        pass
    """
    Returns a new question to ask
    """
    def get_question(self):
        raise NotImplementedError( "Should have implemented this" )
    """
    Returns True if answer is the solution to the question
    """
    def is_correct(self, answer):
        raise NotImplementedError( "Should have implemented this" )

class CountingLevel(Level):
    def __init__(self):
        self.questions_left = 20
    """
    Returns a new question to ask
    """
    def get_question(self):
        self.questions_left = self.questions_left - 1
        self.answer = randint(0, 10) # Number of objects
        # Return in a way for the view to parse and display animals/objects
        self.question = "counting: " + str(self.answer)
        return self.question
    """
    Returns True if answer is the solution to the question
    """
    def is_correct(self, answer):
        try:
            given_answer = int(answer)
        except ValueError:
            return False
        return given_answer == self.answer

class AdditionLevel(Level):
    def __init__(self):
        self.questions_left = 20
    """
    Returns a new question to ask
    """
    def get_question(self):
        self.questions_left = self.questions_left - 1
        self.addend1 = randint(0, 10)
        self.addend2 = randint(0, 10)
        self.answer = self.addend1 + self.addend2
        # Return in a way for the view to parse and display animals/objects
        self.question = "addition: " + str(self.addend1) + " " + str(self.addend2)
        return self.question
    """
    Returns True if answer is the solution to the question
    """
    def is_correct(self, answer):
        try:
            given_answer = int(answer)
        except ValueError:
            return False
        return given_answer == self.answer