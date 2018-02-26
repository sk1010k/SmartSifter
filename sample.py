"""Sample program using smartsifter."""

import numpy as np
import matplotlib.pyplot as plt

from smartsifter import SDEM

np.random.seed(1)

reference_data = np.random.randn(100) # Initialize weights, means and covarinaces of GMM.
test_data = np.random.randn(100)
test_data[50] = 5

sdem = SDEM(1/2, 1.)
sdem.fit(reference_data.reshape(-1,1))

scores = []
for x in test_data:
    x = x.reshape(1,-1)
    sdem.update(x)
    scores.append(-sdem.score_samples(x)) # Score is logarithmic loss.

fig, ax = plt.subplots(2,1)
ax[0].plot(test_data)
ax[0].set_title('Data')
ax[1].plot(scores)
ax[1].set_title('Scores')
plt.show()