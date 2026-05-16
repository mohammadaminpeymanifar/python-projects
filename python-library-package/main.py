from library import Library

def menu():
    lib = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            lib.add_book(title, author)

        elif choice == "2":
            title = input("Enter title to remove: ")
            lib.remove_book(title)

        elif choice == "3":
            title = input("Enter title to search: ")
            lib.search_book(title)

        elif choice == "4":
            lib.show_books()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    menu()