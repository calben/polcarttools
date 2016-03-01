import numpy as np


def cart_to_pol(nparr: np.ndarray) -> np.ndarray:
    r = np.sqrt(nparr[0] ** 2 + nparr[1] ** 2)
    theta = np.arctan2(nparr[1], nparr[0])
    return np.asarray([r, theta])


def pol_to_cart(nparr: np.ndarray) -> np.ndarray:
    x = nparr[0] * np.cos(nparr[1])
    y = nparr[0] * np.sin(nparr[1])
    return np.asarray([x, y])
