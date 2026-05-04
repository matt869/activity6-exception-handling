# Activity 6: Exception Handling
# Basic version - will be improved in later commits

class AppError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def show(self):
        print(f"[ERROR] {self.message}")


class MathError(AppError):
    def __init__(self, message):
        super().__init__(message)

    def show(self):
        print(f"[MATH ERROR] {self.message}")


class InputError(AppError):
    def __init__(self, message):
        super().__init__(message)

    def show(self):
        print(f"[INPUT ERROR] {self.message}")


class FileError(AppError):
    def __init__(self, message):
        super().__init__(message)

    def show(self):
        print(f"[FILE ERROR] {self.message}")


class Calculator:
    def divide(self, a, b):
        try:
            if b == 0:
                raise MathError("Cannot divide by zero!")
            result = a / b
            print(f"{a} / {b} = {result}")
            return result
        except MathError as e:
            e.show()
            return None

    def get_number(self):
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            raise InputError("That is not a valid number!")


class FileHandler:
    def read_file(self, filename):
        try:
            with open(filename, 'r') as f:
                content = f.read()
                print(f"File content:\n{content}")
                return content
        except FileNotFoundError:
            raise FileError(f"File '{filename}' does not exist!")

    def write_file(self, filename, data):
        try:
            with open(filename, 'w') as f:
                f.write(data)
                print(f"Written to {filename} successfully.")
        except IOError:
            raise FileError(f"Could not write to '{filename}'!")


class IndexChecker:
    def __init__(self, items):
        self.items = items

    def get_item(self, index):
        try:
            return self.items[index]
        except IndexError:
            raise AppError(f"Index {index} is out of range! List has {len(self.items)} items.")


def main():
    print("=" * 40)
    print("  Activity 6: Exception Handling")
    print("=" * 40)

    # Test 1: Division
    print("\n--- Test 1: Division ---")
    calc = Calculator()
    calc.divide(10, 2)
    calc.divide(5, 0)

    # Test 2: Input validation
    print("\n--- Test 2: Input Validation ---")
    try:
        calc2 = Calculator()
        num = calc2.get_number()
        print(f"You entered: {num}")
    except InputError as e:
        e.show()

    # Test 3: File handling
    print("\n--- Test 3: File Handling ---")
    fh = FileHandler()
    try:
        fh.write_file("test.txt", "Hello from Activity 6!\n")
        fh.read_file("test.txt")
        fh.read_file("missing.txt")
    except FileError as e:
        e.show()

    # Test 4: Index out of range
    print("\n--- Test 4: Index Out of Range ---")
    checker = IndexChecker([10, 20, 30])
    try:
        print(f"Item at index 1: {checker.get_item(1)}")
        print(f"Item at index 99: {checker.get_item(99)}")
    except AppError as e:
        e.show()

    print("\n" + "=" * 40)
    print("  Done!")
    print("=" * 40)


if __name__ == "__main__":
    main()