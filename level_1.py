def task1() -> None:
    """Створіть програму, яка виводить на екран від 1 до 10."""
    for i in range(1, 11):
        print(i)


def task2() -> None:
    """Запитайте користувача про його ім'я та виведіть привітання з використанням введеної назви."""
    name = input("Enter your name: ")
    print(f"Hello, {name}")


def _input_number(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            ...


def task3() -> None:
    """Створіть програму, яка приймає два числа від користувача та виводить їх суму."""
    a = _input_number("First number: ")
    b = _input_number("Second number: ")

    print(f"Sum of numbers: {a + b}")


def _smallest_num_of_three(a: int, b: int, c: int) -> int:
    return min(a, b, c)


def task4() -> None:
    """Напишіть функцію, яка приймає три параметри (a, b, c) і виводить на екран найменше з них."""
    a = _input_number("First number: ")
    b = _input_number("Second number: ")
    c = _input_number("Third number: ")

    print(f"Smallest number: {_smallest_num_of_three(a, b, c)}")


def main() -> None:
    for idx, fask_func in enumerate((task1, task2, task3, task4), start=1):
        print(f"Task {idx}")
        fask_func()


if __name__ == "__main__":
    main()
