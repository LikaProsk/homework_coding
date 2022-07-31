from lesson_3.file_helpers import read_csv, read_json

from lesson_3.file_helpers import write_json


def books_for_users(path_books_csv: str, path_users_json: str, delimiter: str = ','):
    books = read_csv(path_books_csv, delimiter)
    users = read_json(path_users_json)

    return get_result(books, users)


def get_result(books: list, users: list):
    count_books = len(books)
    count_users = len(users)

    assert count_books != 0 and count_users != 0, "Count_books or count_users is zero"

    result = []
    group_books_for_users = list(func_chunks_generators(books, count_users))

    for group_books in group_books_for_users:
        for i in range(0, len(group_books)):
            if len(result) < count_users:
                add_user_to_result(result, users[i], group_books[i])
            else:
                books = result[i].get("books")
                add_book_to_list(group_books[i], books)

    return result


def add_user_to_result(result: list, user: dict, book: dict = None):
    return result.append({
        "name": user.get("name"),
        "gender": user.get("gender"),
        "address": user.get("address"),
        "age": user.get("address"),
        "books": add_book_to_list(book) if book is not None and len(book) > 0 else []
    })


def add_book_to_list(book: dict, list_book: list = None):
    book = {
        "title": book.get("Title"),
        "author": book.get("Author"),
        "pages": book.get("Pages"),
        "genre": book.get("Genre")
    }

    return list_book.append(book) if list_book is not None else [book]


def func_chunks_generators(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


data = books_for_users("books.csv", "users.json")
write_json("result", data)
