# main.py

import numpy as np
from algorithms.bubble_sort import bubble_sort
from visualization.visualizer import Visualizer


def generate_random_data(size=50):
    """Generate a random list of integers."""
    return np.random.permutation(range(1, size + 1)).tolist()


def main():
    # Generate initial data
    data = generate_random_data(50)

    # Get the bubble sort generator
    sort_gen = bubble_sort(data)

    # Create a Visualizer instance with the data and sorting generator
    viz = Visualizer(data, sort_gen)

    # Start the visualization
    viz.animate()


if __name__ == "__main__":
    main()
