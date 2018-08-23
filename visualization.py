from typing import Optional, Union, Tuple

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray

x_train: Union[ndarray, Tuple[ndarray, Optional[float]]] = np.linspace(-1, 1, 101)
y_train = 2 * x_train + np.random.randn (*x_train.shape) * 0.33

plt.scatter(x_train, y_train)
plt.show()
