import numpy as np
from numpy.random import random

from polcarttools.core import *


def generate_random_points_along_line(origin: np.ndarray, direction: np.ndarray, pool_size: int, points_count: int,
                                      jitter=0.4):
    pool = generate_points_along_line(origin, direction, pool_size)
    jittered_pool = add_jitter_to_points(pool, jitter)
    origins = random.sample(jittered_pool, points_count)
    return origins


def generate_points_along_line(origin, vector_direction, points_count):
    points_on_vector = [np.asarray([i * vector_direction[0] / points_count, vector_direction[1]]) for i in
                        range(points_count)]
    points_on_line = [pol_to_cart(p) for p in points_on_vector]
    points_on_line = [point + origin for point in points_on_line]
    return points_on_line


def add_jitter_to_points(points: [], distribution=np.random.normal, distribution_parameters=[0, 1.0]):
    points = [point + np.asarray([distribution(*distribution_parameters), distribution(*distribution_parameters)]) for
              point in
              points]
    return points
