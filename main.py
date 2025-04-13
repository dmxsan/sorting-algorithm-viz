# main.py

import numpy as np
import matplotlib.pyplot as plt
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from visualization.combined_visualizer import CombinedVisualizer
from visualization.visualizer import Visualizer


def generate_random_data(size=50):
    """Generate a random list of integers."""
    return np.random.permutation(range(1, size + 1)).tolist()


def main():
    # Generate initial data
    data = generate_random_data(50)

    # Get two generators and add data copy to each of them
    bubble_gen = bubble_sort(data.copy())
    insertion_gen = insertion_sort(data.copy())

    # Create and run the combined visualizer
    viz = CombinedVisualizer(data, bubble_gen, data, insertion_gen)
    anim = viz.animate(interval=100, frames=1500)

    # Keep the animation in scope until after plt.show()
    plt.show()
    return anim


if __name__ == "__main__":
    animation_obj = main()
