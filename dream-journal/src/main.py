from utils import save_dream, load_dreams, search_dreams


def menu():
    print("\n🌙 Dream Journal")
    print("1. Add a dream")
    print("2. View all dreams")
    print("3. Search dreams")
    print("4. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            dream = input("Write your dream: ")
            save_dream(dream)
            print("Dream saved!")

        elif choice == "2":
            dreams = load_dreams()
            print("\nYour Dreams:")
            for i, d in enumerate(dreams, 1):
                print(f"{i}. {d}")

        elif choice == "3":
            keyword = input("Enter keyword: ")
            results = search_dreams(keyword)
            print("\nResults:")
            for r in results:
                print(f"- {r}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
Initial commit - project structure
Add main program with menu interface
Implement saving and loading dreams
