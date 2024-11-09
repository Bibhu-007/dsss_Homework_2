import unittest
from math_quiz import random_number_generator, random_operator_generator, arithmetic_problem_and_answer_generator


class TestMathGame(unittest.TestCase):
    """
    Checks the accuracy of the fuctions in math_quiz.py.
    """

    def test_random_number_generator(self):
        """
        Checks 'random_number_generator' function to ensure that it generates a random integer between min_value and max_value.
        """ 
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator_generator(self):
        """
        Checks 'random_operator_generator' function to ensure it generates only allowed operators i.e. '+', '-', or '*'.
        """
        for _ in range(1000):
             operator = random_operator_generator()
             self.assertIn(operator, ['+', '-', '*'])

    def test_arithmetic_problem_and_answer_generator(self):
        """
        Checks 'arithmetic_problem_and_answer_generator' to ensure it generates the correct arithmetic problems and answers.
        """
        # Defines test cases as tuples ()
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 2, '+', '10 + 2', 12),
            (2, 10, '-', '2 - 10', -8),
            (2, 10, '*', '2 * 10', 20)
        ]
        
        for number_1, number_2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = arithmetic_problem_and_answer_generator(number_1, number_2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
