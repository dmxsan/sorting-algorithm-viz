# visualization/visualizer.py

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Visualizer:
    def __init__(self, data, sort_gen):
        self.data = data
        self.sort_gen = sort_gen
        self.fig, self.ax = plt.subplots()
        self.bar_rects = self.ax.bar(range(len(data)), data, align="edge")
        self.ax.set_title("Sorting Algorithm Visualization")
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Value")

    def update(self, _):
        try:
            # Get the next state of the list from the sorting generator
            self.data = next(self.sort_gen)
        except StopIteration:
            # If sorting is complete, stop the animation (or keep the final state)
            return self.bar_rects

        # Update the heights of bars based on new data
        for rect, val in zip(self.bar_rects, self.data):
            rect.set_height(val)
        return self.bar_rects

    def animate(self):
        anim = animation.FuncAnimation(
            self.fig,
            self.update,
            frames=200,  # This can be set based on your needs
            interval=100,  # Update interval in milliseconds
            blit=False,
            repeat=False
        )
        plt.show()
