
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
        print("[TODO] Add book")
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