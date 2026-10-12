var = "The BodyGuard"

print("Positive indexes:")
for i in range(len(var)):
    print(f"var[{i}]: {var[i]}")

print("\nNegative indexes:")
for i in range(len(var) * -1, 0):
    print(f"var[{i}]: {var[i]}")

print(f"\nUpper Case: {var.upper()}")
print(f"\nLower Case: {var.lower()}")
print(f"\nSwap Case: {var.swapcase()}")
print(f"\nCase Fold: {var.casefold()}")

print(f"\nFind char sequence: {var.lower().find('guard')}")

print(f"\nSplit String by 'space':")
print(var.split())

print(f"\nSplit String by 'y':")
print(var.split("y"))