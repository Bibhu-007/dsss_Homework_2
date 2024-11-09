import random


def random_number_generator(min_value, max_value):
    """
    Generates a random integer between min_value and max_value.

    Parameters
    ----------
    min_value : int
        The minimum value for the random integer.
    max_value : int
        The maximum value for the random integer.

    Returns
    -------
    int
        A random integer between min_value and max_value.  
    """
    return random.randint(min_value, max_value)


def random_operator_generator():
    """
    Generates a random arithmetic operator.

    Returns
    -------
    str
        A random arithmetic operator among "+", "-", or "*".
    """
    
    return random.choice(['+', '-', '*'])


def arithmetic_problem_and_answer_generator(number_1, number_2, operator):
    """
    Generates a random arithmetic problem and its solution.

    Parameters
    ----------
    number_1 : int
        The first number
    number_2 : int 
        The second number
    operator : str
        The arithmetic operator('+', '-', or '*')

    Returns
    -------
    str and int
        problem : str
            A string representing the arithmetic problem.
        answer : int
            The correct answer to the arithmetic problem.
    """
    problem = f"{number_1} {operator} {number_2}"
    if operator == '+':
        answer = number_1 + number_2
    elif operator == '-':
        answer = number_1 - number_2
    else: # operator = "*"
        answer = number_1 * number_2
    return problem, answer

def math_quiz():
    """
    Generates arithmetic problems for the user to solve, checks the answers and gives a score.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number_1 = random_number_generator(1, 10)
        number_2 = random_number_generator(1, 5)
        operator = random_operator_generator()

        problem, answer = arithmetic_problem_and_answer_generator(number_1, number_2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid Input! Please enter an integer.")            

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()