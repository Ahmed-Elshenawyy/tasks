def calculate_factorial():
    n = int(input("Enter a positive integer N: "))
    result = 1
    for i in range(1, n + 1):
        result = result * i
    print("The factorial of", n, "is", result)

calculate_factorial()