from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    title: str
    author: str
    publication_year: int
    isbn: str


@dataclass
class Library:
    books_list: List[Book]

    def add_book(self, book: Book) -> None:
        self.books_list.append(book)

    def delete_book(self, isbn: str) -> None:
        for count, book in enumerate(self.books_list):
            if isbn == book.isbn:
                del self.books_list[count]

    def search_by_title(self, title: str) -> List[Book]:
        for book in self.books_list:
            if title == book.title:
                return book

    def search_by_author(self, author: str) -> List[Book]:
        for book in self.books_list:
            if author == book.author:
                return book

    def display_books(self) -> None:
        for book in self.books_list:
            print(
                f"{book.title} written by {book.author}. This books is written in {book.publication_year}. It's ISBN code - {book.isbn}"
            )


book_one = Book(
    title="Hamlet",
    author="William Shakespeare",
    publication_year=1601,
    isbn="978-0812036381",
)
book_two = Book(
    title="A Game Of Thrones",
    author="George R. Martin",
    publication_year=1996,
    isbn="978-0553573404",
)
book_three = Book(
    title="The Lord of the Rings The Ring Sets Out",
    author="J.R.R. Tolkien",
    publication_year=1937,
    isbn="978-0007123810",
)
book_four = Book(
    title="Things Fall Apart",
    author="Chinua Achebe",
    publication_year=1958,
    isbn="978-0385474542",
)

library = Library(books_list=[book_one, book_two, book_three])
library.add_book(book_four)

print(library.display_books())
