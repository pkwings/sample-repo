# Sample Python Code: Greeting Names

def greet_names(names):
    for name in names:
        print(f"Hello, {name}!")

def main():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    greet_names(names)
    print(f"Total names greeted: {len(names)}")

if __name__ == "__main__":
    main()
