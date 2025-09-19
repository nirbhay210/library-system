
books = []
next_book_id = 1


class Book:
    def __init__(self, id: int, title: str, author: str, available: bool = True):
        self.id = id
        self.title = title
        self.author = author
        self.available = available

    def __repr__(self) -> str:
        return f"<Book {self.id}: {self.title} by {self.author}, available ={self.available}>"


def _read_nonempty(prompt: str) -> str:
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty.")


def add_book() -> None:
    global next_book_id
    title = _read_nonempty("Enter book title: ")
    author = _read_nonempty("Enter author name: ")


    book = Book(id=next_book_id, title=title, author=author)
    books.append(book)
    print(f"Added Book #{next_book_id}: {title} by {author}")
    next_book_id += 1



def print_menu():
    print("\n=== Library System ===")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View All")
    print("q. Quit")

def handler_choice(choice: str) -> None:
    if choice == "1":
        add_book()
    elif choice == "2":
        print("[TODO] Add member")
    elif choice == "3":
        print("[TODO] Borrow Book")
    elif choice == "4":
        print("[TODO] Return Book")
    elif choice == "5":
        print("[TODO] View All")
    elif choice == "q":
        print("Goodbye!")
        raise SystemExit
    else:
        print("Invalid choice.")



def main():
    while True:
        print_menu()
        choice = input("chose an operation").strip().lower()
        handler_choice(choice)



if __name__ == "__main__":
    main()