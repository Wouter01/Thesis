import matplotlib.pyplot as plt
import numpy as np

# Function to read data from a file
def read_durations_from_file(filename):
    with open(filename, 'r') as file:
        return [float(line.strip()) for line in file]

# Function to calculate and annotate statistics
def annotate_stats(data, box, ax, positions):
    for i, (d, pos) in enumerate(zip(data, positions)):
        q1 = np.percentile(d, 25)
        avg = np.mean(d)
        q3 = np.percentile(d, 75)
        median = np.median(d)

        # Annotate Q1
        ax.text(pos, q1, f'Q1: {q1:.2f}', horizontalalignment='right', verticalalignment='top', color='blue')
        # Annotate average
        ax.text(pos, avg, f'Avg: {avg:.2f}      ', horizontalalignment='right', verticalalignment='center', color='red')
        # Annotate Q3
        ax.text(pos, q3, f'Q3: {q3:.2f}', horizontalalignment='right', verticalalignment='bottom', color='green')

        ax.text(pos, median, f'Median: {median:.2f}      ', horizontalalignment='right', verticalalignment='bottom', color='darkorange')

# Read data from files
durations1 = read_durations_from_file('arduino/durations_64_bytes_1_000_000.txt')
durations2 = read_durations_from_file('arduino/durations_wasi_64_bytes_1_000_000.txt')

# durations1 = [d for d in durations1 if d < 3000]
# durations2 = [d for d in durations2 if d < 3000]

# Combine the data into a list of arrays
data = [durations1, durations2]

# Create the boxplot
# plt.figure(figsize=(6, 6))
fig, ax = plt.subplots(figsize=(8, 6))
box = ax.boxplot(data, patch_artist=True, vert=True, labels=['Native', 'WASI'])



annotate_stats(data, box, ax, positions=[1, 2])
plt.yscale('log')

# Add title and labels
plt.ylabel('Duration (microseconds)')

# Show the plot
plt.show()