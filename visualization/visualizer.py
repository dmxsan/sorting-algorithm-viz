import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Visualizer:
    def __init__(self, data):
        self.data = data
        self.fig, self.ax = plt.subplots()
        self.bar_rects = self.ax.bar(range(len(data)), data, align="edge")
        self.ax.set_title("Sorting Algorithm Visualization")
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Value")

    def update(self, frame):
        """Update the bar heights for the animation. This is a placeholder for sorting steps."""
        # For now, we'll just reverse the data as a sample animation.
        self.data = self.data[::-1]
        for rect, val in zip(self.bar_rects, self.data):
            rect.set_height(val)
        return self.bar_rects

    def animate(self):
        """Animate the visualization."""
        anim = animation.FuncAnimation(
            self.fig,
            self.update,
            frames=100,  # adjust based on expected number of sorting steps
            interval=100,  # update interval in milliseconds
            blit=False,
            repeat=False
        )
        plt.show()
