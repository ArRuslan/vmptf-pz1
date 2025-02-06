def _input_number(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            ...

def task1() -> None:
    """Напишіть програму, яка знаходить середнє значення з трьох чисел, введених користувачем."""
    a = _input_number("First number: ")
    b = _input_number("Second number: ")
    c = _input_number("Third number: ")

    avg = (a + b + c) / 3

    print(f"Average: {avg}")


def task2() -> None:
    """Створіть список чисел від 1 до 20. Виведіть на екран кожне число та його квадрат."""
    nums = list(range(1, 21))

    for num in nums:
        print(f"{num} - {num ** 2}")


def task3() -> None:
    """Реалізуйте програму, яка визначає, чи є введене користувачем число простим."""
    num = _input_number("Enter a number: ")
    if num <= 3:
        return print(f"{num} is a prime number")
    if num % 2 == 0:
        return print(f"{num} is not a prime number")

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return print(f"{num} is not a prime number")

    print(f"{num} is a prime number")


def task4() -> None:
    """Напишіть функцію, яка приймає рядок та повертає його обернений варіант. Наприклад, "hello" повинно повернути "olleh"."""
    s = input("Enter something: ")
    print(f"Reversed string: {s[::-1]}")


def main() -> None:
    for idx, fask_func in enumerate((task1, task2, task3, task4), start=1):
        print(f"Task {idx}")
        fask_func()


if __name__ == "__main__":
    main()
