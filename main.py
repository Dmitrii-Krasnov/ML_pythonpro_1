"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

MAX = 100  # максимально возможное для загадывания число


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left = 0
    right = MAX + 1

    while True:
        count += 1
        predict_number = np.random.randint(left, right)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif predict_number > number:
            right = predict_number  # сдвигаем правую границу ближе к загаданнаму числу
        else:
            left = predict_number  # сдвигаем левую границу ближе к загаданнаму числу
    return count


def score_game(random_predict_func) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict_func ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, MAX + 1, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
