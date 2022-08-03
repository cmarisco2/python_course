from math import cos, sin
import numpy as np


def roll(vec_A, vec_B):
    vector_a = np.squeeze(np.asarray(vec_A))
    # vector_a = np.array(*vec_A)

    # flipped
    vector_b = np.squeeze(np.asarray([0 - point for point in vec_B]))

    # connecting vector
    vector_c = vector_b + vector_a

    # print(vector_c)

    scalar_prod = vector_b.dot(vector_c)
    print(scalar_prod)

    mag_b = np.linalg.norm(vector_b)
    mag_c = np.linalg.norm(vector_c)
    # print(mag_c)
    # print(mag_b)

    angle = np.arccos(scalar_prod/(mag_b * mag_c))

    return np.rad2deg(angle)


# NEED LOCATION FOR LEFT AND RIGHT
vecB = np.array([0, 4])
vecA = np.array([2, 1])
scale = vecA.dot(vecB)
print(scale)
angle = roll(vecA, vecB)
print(angle)
print(cos(angle))

print()

vecA = np.array([-2, 1])
scale = vecA.dot(vecB)
print(scale)
angle = roll(vecA, vecB)
print(angle)
print(cos(angle))
