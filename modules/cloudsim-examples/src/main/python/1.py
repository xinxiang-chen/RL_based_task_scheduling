import matplotlib.pyplot as plt
import numpy as np

# Parameters
epsilon_start = 0.9
epsilon_end = 0.1
max_iterations = 1000

# Compute epsilon for each iteration
iterations = np.arange(max_iterations + 1)
epsilon_t = np.maximum(
    epsilon_end,
    epsilon_start - (epsilon_start - epsilon_end) * (iterations / max_iterations)
)

# Plot
plt.figure(figsize=(8, 4))
plt.plot(iterations, epsilon_t, label=r'$\epsilon_t$')
plt.xlabel('Iteration', fontsize=24)
plt.ylabel('Epsilon', fontsize=24)
# plt.title('Epsilon decay over iterations')
plt.grid(True)
plt.legend(fontsize=22)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.tight_layout()
plt.show()
