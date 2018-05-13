""" Linear Algebra """

# Getting to magnitude

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

from functools import reduce

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the ith elements of
    the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v,w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v,w)

def sum_of_squares(v):
    return dot(v, v)

import math

def magnitude(v):
    """magnitude, length or euclidean norm (length) of a vector is the distance
    between the tail and its tip"""
    return math.sqrt(sum_of_squares(v))

# Getting to distance
""" 
Now we have what we need to compute the distance between two vectors defined:
    distance = sqrt( (v1 - w1)^2 + .... + (vn - wn)^2 )
"""
def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

""" STATISTICS """

# Central Tendencies

def mean(v):
    return sum(v)/len(v)

def median(v):
    n = len(v)
    sorted_v = sorted(v)

    # only a midpoint if v is even length
    midpoint = n // 2

    if n % 2 = 1:
        return sorted_v[midpoint]
    else:
        return (sorted_v[midpoint-1] + sorted_v[midpoint]) / 2

def quantile(x, p):
    """returns the pth-percentile value in x"""
    sorted_x = sorted(x)
    # round p_index to base int
    p_index = int(p * len(x))
    return sorted_x[p_index] 

# Dispersion

""" why do we need variance?
TODO
"""
def deviations_from_mean(x):
    x_bar = mean(x)  
    return [x_i - x_bar for x_i in x]

def variance(x):
    """ sum of list of squared deviations from mean"""
    """ note - why n-1?: since we are likely looking at a sample, x_bar is only an
    estimate of the actual mean, which means that on average (x_i - x_bar) ** 2
    is an underestimate of x_i's squared deviation from the mean, which is why
    we divide by n-1 instead of n (see bit.ly/lL2EapI)"""
    n = len(x)
    deviations = deviations_from_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

""" standard deviation suffers from the same outlier problem that mean does so
a more robust alternative computes the difference between the 75th percentile
and the 25th percentile"""

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

# Correlation

""" why do we need covariance?
wheres variance measures how a single variable deviates from its mean,
covariance measures how two variables vary in tandem from their means"""

def covariance(x, y):
    """remember that dot sums up the products of corresponding pairs of
    elements. When the responding elements are both above or below their means,
    a positive number enters the sum, if they are on opposite sides of their
    means, a negative number enters the sum"""
    n = len(x)
    return dot(deviations_from_mean(x), deviations_from_mean(y))/ (n - 1)

""" why do we need correlation?
covariance by itself is a number that needs context: numbers that are
absolutely larger have a larger covariance.
correlation divides out the standard deviations of both variables"""

def correlation(x, y):
    """correlation is unitless and always lies between -1 (perfect
    anti-correlation) and 1 (perfect correlation)"""
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

""" extremes of correlation: 
zero correlation:
    x = [-2, -1, 0, 1, 2]
    y = [2, 1, 0, 1, 2]

perfect correlation:
    x = [-2, -1, 0, 1, 2]
    y = [99.98, 99.99, 100, 100.01, 100.02]
"""


