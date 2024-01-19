import random

def generate_math_question(min_num: int, max_num: int) -> str:
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    operators = ['+', '-', '/', '*']
    index = random.randint(0, len(operators) - 1)
    math_question = f'{num1} {operators[index]} {num2}'
    return math_question


def check_answer(question: str, answer: str) -> bool:
    try:
        return float(answer) == eval(question)
    except ValueError:
        return False


# предыдущие функции добавлены скрыто для тестов

def math_quiz(number_of_questions: int = 5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0
    for i in range(number_of_questions):
        question = generate_math_question(1, 7)
        user_answer = input(f"{question} = ")
        if check_answer(question, user_answer):
            correct_answers += 1


    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")
    percentages = correct_answers / number_of_questions * 100
    if percentages >= 80:
        print("Отлично! Вы получаете оценку A.")
    elif percentages >= 60:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


# Запуск теста
math_quiz(10)