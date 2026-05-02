def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Input
n = int(input("Enter number of terms: "))
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
    