def _input_number(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            ...


class Book:
    __slots__ = ("name", "author", "year",)

    def __init__(self, name: str, author: str, year: int) -> None:
        self.name = name
        self.author = author
        self.year = year


def task1() -> None:
    """Напишіть клас "Книга" з властивостями, такими як назва, автор та рік видання. Створіть об'єкт цього класу та виведіть його характеристики."""
    book = Book(
        input("Book name: "),
        input("Book author: "),
        _input_number("Book year: "),
    )

    print(f"Book: {book.name=}, {book.author=}, {book.year=}")


def task2() -> None:
    """Реалізуйте програму для роботи з API. Використовуйте бібліотеку requests, щоб отримати дані з публічного API та вивести їх на екран."""
    import requests

    resp = requests.get("https://httpbin.org/ip")
    ip = resp.json()["origin"]
    print(f"Ip address: {ip}")


class Library:
    __slots__ = ("_books",)

    def __init__(self) -> None:
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, book_idx: int) -> None:
        del self._books[book_idx]

    def get_books(self) -> list[Book]:
        return self._books


def task3() -> None:
    """Створіть клас "Книготека" з можливістю додавання та видалення книг, а також виведення списку усіх книг."""
    lib = Library()

    options = "0. Exit\n1. Add new book\n2. Remove book\n3. Print books\n> "
    while (op := input(options)) != "0":
        match op:
            case "1":
                lib.add_book(Book(
                    input("Book name: "),
                    input("Book author: "),
                    _input_number("Book year: "),
                ))
            case "2":
                idx = _input_number("Book index: ")
                lib.remove_book(idx)
            case "3":
                for idx, book in enumerate(lib.get_books()):
                    print(f"Book #{idx}: {book.name=}, {book.author=}, {book.year=}")


def _qs_partition(nums: list[int], lo: int = None, hi: int = None) -> int:
    pivot = nums[hi]

    i = lo
    for j in range(lo, hi):
        if nums[j] > pivot:
            continue
        nums[i], nums[j] = nums[j], nums[i]
        i += 1

    nums[i], nums[hi] = nums[hi], nums[i]
    return i


def _quicksort(nums: list[int], lo: int = None, hi: int = None) -> list[int]:
    if lo is None or hi is None:
        lo = 0
        hi = len(nums) - 1

    if lo >= hi or lo < 0:
        return nums

    p = _qs_partition(nums, lo, hi)

    _quicksort(nums, lo, p - 1)
    _quicksort(nums, p + 1, hi)

    return nums


def task4() -> None:
    """Розробіть алгоритм сортування масиву чисел методом швидкого сортування (QuickSort) та виведіть відсортований масив."""
    nums = []
    while True:
        try:
            nums.append(_input_number("Enter a number: "))
        except KeyboardInterrupt:
            break

    print(f"Numbers: {nums}")
    print(f"Numbers sorted: {_quicksort(nums)}")


def main() -> None:
    for idx, fask_func in enumerate((task1, task2, task3, task4), start=1):
        print(f"Task {idx}")
        fask_func()


if __name__ == "__main__":
    main()
