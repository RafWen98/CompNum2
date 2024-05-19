import numpy as np
import matplotlib.pyplot as plt

def chebyshev_nodes_first_kind(n):
    return np.cos((2 * np.arange(1, n + 1) - 1) / (2 * n) * np.pi)

def chebyshev_nodes_second_kind(n):
    return np.cos(np.arange(n + 1) * np.pi / n)

# Number of nodes
n = 8

# Compute Chebyshev nodes
nodes_first_kind = chebyshev_nodes_first_kind(n)
nodes_second_kind = chebyshev_nodes_second_kind(n)

# Create the plot
fig, axes = plt.subplots(2, 1, figsize=(8, 10))

# Plot for the first kind
axes[0].plot(nodes_first_kind, np.sqrt(1 - nodes_first_kind**2), 'o', color='blue')
axes[0].vlines(nodes_first_kind, 0, np.sqrt(1 - nodes_first_kind**2), colors='blue')
axes[0].plot(nodes_first_kind, -np.sqrt(1 - nodes_first_kind**2), 'o', color='purple')
axes[0].vlines(nodes_first_kind, 0, -np.sqrt(1 - nodes_first_kind**2), colors='purple')
axes[0].plot(np.linspace(-1, 1, 100), np.sqrt(1 - np.linspace(-1, 1, 100)**2), color='black')
axes[0].plot(np.linspace(-1, 1, 100), -np.sqrt(1 - np.linspace(-1, 1, 100)**2), color='black', linestyle='dashed')
axes[0].set_title(f'Chebyshev Nodes of the First Kind for n = {n}')
axes[0].set_xlabel('$x$')
axes[0].set_ylabel('$y$')
axes[0].set_xlim(-1.1, 1.1)
axes[0].set_ylim(-1.1, 1.1)
axes[0].grid(True)

# Plot for the second kind
axes[1].plot(nodes_second_kind, np.sqrt(1 - nodes_second_kind**2), 'o', color='blue')
axes[1].vlines(nodes_second_kind, 0, np.sqrt(1 - nodes_second_kind**2), colors='blue')
axes[1].plot(nodes_second_kind, -np.sqrt(1 - nodes_second_kind**2), 'o', color='purple')
axes[1].vlines(nodes_second_kind, 0, -np.sqrt(1 - nodes_second_kind**2), colors='purple')
axes[1].plot(np.linspace(-1, 1, 100), np.sqrt(1 - np.linspace(-1, 1, 100)**2), color='black')
axes[1].plot(np.linspace(-1, 1, 100), -np.sqrt(1 - np.linspace(-1, 1, 100)**2), color='black', linestyle='dashed')
axes[1].set_title(f'Chebyshev Nodes of the Second Kind for n = {n}')
axes[1].set_xlabel('$x$')
axes[1].set_ylabel('$y$')
axes[1].set_xlim(-1.1, 1.1)
axes[1].set_ylim(-1.1, 1.1)
axes[1].grid(True)


plt.tight_layout()
plt.savefig("figs/cheby_nodes.png")
plt.show()
