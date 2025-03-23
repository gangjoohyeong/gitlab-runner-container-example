import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

sum_arr = arr1 + arr2
mul_arr = arr1 * arr2
dot_product = np.dot(arr1, arr2)

print("Sum of two arrays: ", sum_arr)
print("Multiplication of two arrays: ", mul_arr)
print("Dot product of two arrays: ", dot_product)
