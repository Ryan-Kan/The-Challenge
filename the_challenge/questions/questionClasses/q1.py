"""
q1.py

Created on 2020-08-21
Updated on 2020-10-24

Copyright Ryan Kan 2020

Description: A file which holds the designated question class.
"""

# IMPORTS
from the_challenge.misc import mathematical_round
from the_challenge.questions.questionClasses.questionBaseClass import Question


# CLASSES
class Q1(Question):
    """
    Q1:
    Addition, subtraction, multiplication or division of two small numbers.
    """

    def calculations(self):
        # CONSTANTS
        operators = ["+", "-", "*", "/"]

        # CALCULATIONS
        a = self.random.randint(1, 20)
        b = self.random.randint(1, 20)

        self.question = f"{a} {self.random.choice(operators)} {b}"
        self.answer = mathematical_round(eval(self.question), 3)

    def generate_question(self):
        treated_expr = self.question.replace("*", "\\times").replace("/", "\\div")
        string = f"State the value of $${treated_expr}$$"

        return string

    def generate_answer(self):
        return self.answer

    def generate_input_fields_prefixes(self):
        return ["Answer:"]


# DEBUG CODE
if __name__ == "__main__":
    question = Q1(seed_value=1123581321)
    question.calculations()
    print(question.generate_question())
    print("[ANSWER]", question.generate_answer())
