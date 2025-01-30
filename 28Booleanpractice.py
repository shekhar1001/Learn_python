def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    try:
        user_input = int(input("Enter a number: "))
        result = check_even_odd(user_input)
        print(f"The number {user_input} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
