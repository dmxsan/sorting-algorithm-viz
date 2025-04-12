import matplotlib.pyplot as plt
import numpy as np
from visualization.visualizer import Visualizer


def generate_random_data(size=50):
    """Generate a random list of integers."""
    return np.random.permutation(range(1, size + 1)).tolist()


def main():
    # Generate initial data
    data = generate_random_data(50)

    # Create a Visualizer instance
    viz = Visualizer(data)

    # Start the visualization (this will launch the animated window)
    viz.animate()


if __name__ == "__main__":
    main()
