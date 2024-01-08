import numpy as np

# one-dimensional array
one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(one_dimensional_array)

# two-dimensional array
two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)

# sequence of integers
sequence_of_integers = np.arange(5, 12)
print(sequence_of_integers)

# random integers
random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
print(random_integers_between_50_and_100)

# random floats
random_floats_between_0_and_1 = np.random.random([6])
print(random_floats_between_0_and_1)

# random floats
random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print(random_floats_between_2_and_3)

# random floats
random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print(random_integers_between_150_and_300)

# ----------------------------------------------------------------

# Add feature
feature = np.arange(6, 21)
print(feature)
label = (3) * (feature) + 4
print(label)

# Add random noise
noise = (np.random.random([15]) * 4) - 2
print(noise)
label = label + noise
print(label)
