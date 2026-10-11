import numpy as np
import matplotlib.pyplot as plt

print("Create a numpy array")
a = np.array([0, 1, 2, 3, 4])
print(a)

print("\nRetrieve each element of the np array")
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(f"\nRetrieve numpy version: {np.__version__}")
print(f"Checking numpy array type: {type(a)}")
print(f"Checking type of values stored within the numpy array: {a.dtype}")

print("\nAssigning values to the the numpy array")
print(a)
a[0] = 5
print(a)

print(f"\nSlicing a numpy array/Making a sub numpy array: {a[1:4]}")
print(f"Slicing a numpy array/Making a sub numpy array using steps: {a[1:4:2]}")
print(f"Slicing a numpy array/Making a sub numpy array without starting index: {a[:4]}")
print(f"Slicing a numpy array/Making a sub numpy array without endinf index: {a[4:]}")
print(f"Slicing a numpy array/Making a sub numpy array without steps: {a[1:4:]}")

print(f"\nSelecting numpy array elements using a list: {a[[0, 2, 3, 4]]}")

print("\nAssign a value to multiple numpy array elements at the same time")
a[[0, 2, 3, 4]] = 1000
print(a)

print("\nNumpy Other Attributes:")
print(f"Getting the numpy array size: {a.size}")
print(f"Getting the number of dimensions of a numpy array: {a.ndim}")
print(f"Getting the shape of dimensions of a numpy array: {a.shape}")

print("\nNumpy Statistical Functions:")
print(f"Getting arithmetic average (mean()) of a numpy array: {a.mean()}")
print(f"Getting standard deviation of a numpy array: {a.std()}")
print(f"Getting the max value within a numpy array: {a.max()}")
print(f"Getting the min value within a numpy array: {a.min()}")

print("\nNumpy Array Operations:")
a1 = np.array([0, 1])
a2 = np.array([1, 2])

print(f"Adding '{a1}' and '{a2}' numpy arrays: {np.add(a1, a2)}")
print(f"Subtracting '{a1}' and '{a2}' numpy arrays: {np.subtract(a1, a2)}")
print(f"Multiplying '{a1}' and '{a2}' numpy arrays: {np.multiply(a1, a2)}")
print(f"Dividing '{a1}' and '{a2}' numpy arrays: {np.divide(a1, a2)}")
print(f"Getting the dot product of '{a1}' and '{a2}' numpy arrays: {np.dot(a1, a2)}") # (a1[0] * a2[0]) + ... + (a1[n] * a2[n])
print(f"Adding a constant to '{a1}' numpy array: {a1 + 1}") # [a1[0] + 1, ..., a1[n] + 1]

print("\nNumpy Mathematical Functions:")
print(f"Getting the value of 'pi': {np.pi}")
print(f"Getting the result of the 'sin' of '{a}': {np.sin(a)}")

print("\nNumpy Linspace:")
print(f"Getting 5 evenly spaced numbers over a specified interval: {np.linspace(-2, 2, num=5)}")
print(f"Getting 9 evenly spaced numbers over a specified interval: {np.linspace(-2, 2, num=9)}")
print(f"Getting the plot result of {np.linspace(0, 2*np.pi, num=2)} and {np.sin(np.linspace(0, 2*np.pi, num=2))}: {plt.plot(np.linspace(0, 2*np.pi, num=100), np.sin(np.linspace(0, 2*np.pi, num=100)))}")

print("\nIterating 1-D Numpy Arrays:")
for ai in a:
    print(ai)