import random
import matplotlib.pyplot as plt

def random_walk():
    """A generator for a random walk with step size 1.
    Walks up or down with equal probability, and stops when displacement = ±10."""
    
    position = 0  # start at origin
    while abs(position) < 10:  # stop when displacement reaches 10
        step = random.randint(0, 1)  # random step: 0 or 1
        if step == 0:
            position -= 1  # move down
        else:
            position += 1  # move up
        yield position  # yield current position each step

# Collect the walk data
positions = [0]  # start from 0
for pos in random_walk():
    positions.append(pos)

# Create a list of step numbers for the x-axis
steps = list(range(len(positions)))

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(steps, positions, marker='o', linestyle='-', linewidth=2)
plt.title("Random Walk (Step Size = 1)")
plt.xlabel("Step Number")
plt.ylabel("Position")
plt.grid(True)
plt.show()
