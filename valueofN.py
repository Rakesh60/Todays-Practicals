def compute_value(n):
    n1 = int(str(n))
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    return n1 + n2 + n3

# Example usage:
n = int(input("Enter an integer: "))
result = compute_value(n)
print("The result of n+nn+nnn is:", result)
