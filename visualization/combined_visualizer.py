import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.core.pylabtools import figsize


class CombinedVisualizer:
    def __init__(self, data1, gen1, data2, gen2):
        # Copy of data for each sorting algorithm
        self.data1 = data1.copy() # Data for first sort algorithm
        self.gen1 = gen1 # Generator for first sort algorithm

        self.data2 = data2.copy()  # Data for second sort algorithm
        self.gen2 = gen2  # Generator for second sort algorithm

        # Get title from the sorting algorithm's name
        title1 = self._get_title_from_generator(gen1)
        title2 = self._get_title_from_generator(gen2)

        # Create a figure side-by-side
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(12,6))

        # Setup first subplot
        self.bars1 = self.ax1.bar(range(len(self.data1)), self.data1, align="edge")
        self.ax1.set_title(title1)
        self.ax1.set_xlabel("Index")
        self.ax1.set_ylabel("Value")

        # Setup first subplot
        self.bars2 = self.ax2.bar(range(len(self.data2)), self.data2, align="edge")
        self.ax2.set_title(title2)
        self.ax2.set_xlabel("Index")
        self.ax2.set_ylabel("Value")

    def _get_title_from_generator(self, gen):
        """Extract and format the sort algorithm's name from the generator"""
        try:
            # Get the function name from the generator's frame
            func_name = gen.gi_frame.f_code.co_name
            # Replace underscores with spaces and convert to title case
            return func_name.replace('_', ' ').title()
        except Exception:
            return "Sort Algorithm"

    def update(self, frame):
        # Update first subplot from generator 1
        try:
            self.data1 = next(self.gen1)
            for bar, value in zip(self.bars1, self.data1):
                bar.set_height(value)
        except StopIteration:
            pass

        # Update second subplot from generator 2
        try:
            self.data2 = next(self.gen2)
            for bar, value in zip(self.bars2, self.data2):
                bar.set_height(value)
        except StopIteration:
            pass

        # Return updated bars
        return self.bars1 + self.bars2

    def animate(self, interval=100, frames=200): # Default parameter value
        self.anim = animation.FuncAnimation(
            self.fig,
            self.update,
            frames=frames,
            interval=interval,
            repeat=False
        )
        return self.anim # return it so the caller can hold it
