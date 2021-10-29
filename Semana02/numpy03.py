import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([2,4,6,8,10])
a1[2]
a1[:-2]
a1[1:-2]
a1>3

names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])
first_letter_j = np.vectorize(lambda s: s[0])(names)=='J'
np.vectorize(lambda s: s[0])(names)
a1%4
