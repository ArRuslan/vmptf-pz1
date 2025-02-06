from datetime import date


def _input_number(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            ...


def task1() -> None:
    """Реалізуйте програму, яка приймає на вхід рік народження користувача та виводить його вік."""
    year = _input_number("Your birth year: ")
    print(f"You are (probably) {date.today().year - year} years old")


def _get_numbers_divisible_by_two(nums: list[int]) -> list[int]:
    return list(filter(lambda num: num % 2 == 0, nums))


def task2() -> None:
    """Створіть функцію, яка приймає список чисел та повертає новий список, який містить лише парні числа."""
    nums = []
    while True:
        try:
            nums.append(_input_number("Enter a number: "))
        except KeyboardInterrupt:
            break

    print(f"Numbers: {nums}")
    print(f"Numbers divisible by 2: {_get_numbers_divisible_by_two(nums)}")


def task3() -> None:
    """Створіть клас "Калькулятор" з методами для додавання, віднімання, множення та ділення. Виведіть результат обчислень для певного прикладу."""
    a = _input_number("First number: ")
    b = _input_number("Second number: ")
    while (op := input("Operation: ")) not in ("+", "-", "*", "/"):
        ...

    result = None
    match op:
        case "+":
            result = a + b
        case "-":
            result = a - b
        case "*":
            result = a * b
        case "/":
            if b == 0:
                return print("Second number (divisor) is zero!")
            result = a / b

    print(f"Result: {result}")


def task4() -> None:
    """Реалізуйте програму, яка визначає, чи є слово паліндромом (читається однаково з обох боків)."""
    s = input("Enter something: ")
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return print(f"{s!r} is not a palindrome!")

    print(f"{s!r} is a palindrome!")


def main() -> None:
    for idx, fask_func in enumerate((task1, task2, task3, task4), start=1):
        print(f"Task {idx}")
        fask_func()


if __name__ == "__main__":
    main()
