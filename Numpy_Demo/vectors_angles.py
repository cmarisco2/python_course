import numpy as np


# demo basic numpy with vectors
# a = <2, 2, -1> and b = <5, -3, 2> BOTH Position Vectors
# angle between them is defined by dot product
# cos(theta) = a*b/(|a||b|)
# theta = arccos([above argument])
# should get ~1.46 radians or 84 degrees

a = np.array([2, 2, -1])
b = np.array([5, -3, 2])

scalar_product = a.dot(b)
mag_a = np.linalg.norm(a)
mag_b = np.linalg.norm(b)


angle = np.arccos(scalar_product/(mag_a * mag_b))
angle = round(angle, 2)
print(f'angle in radians: {angle}')
print(f'angle in degrees: {round(np.rad2deg(angle), 2)}')
