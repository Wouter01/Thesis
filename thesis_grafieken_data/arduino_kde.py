import pandas as pd
import numpy as np

# Load data from files
wasi_data = pd.read_csv('arduino/durations_wasi_64_bytes_1_000_000.txt', header=None, names=['Time'])
native_data = pd.read_csv('arduino/durations_64_bytes_1_000_000.txt', header=None, names=['Time'])

wasi_data = wasi_data[wasi_data['Time'] <= 2000]
native_data = native_data[native_data['Time'] <= 2000]

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.stats import gaussian_kde

# Function to find peaks in KDE
def find_kde_peaks(data, bandwidth=0.1):
    kde = gaussian_kde(data, bw_method=bandwidth)
    x = np.linspace(data.min(), data.max(), 1000)
    kde_values = kde(x)
    peaks, _ = find_peaks(kde_values)
    return x, kde, peaks

x1, kde1, peaks1 = find_kde_peaks(wasi_data['Time'])
x2, kde2, peaks2 = find_kde_peaks(native_data['Time'])

# Create a KDE plot for each file's data
sns.kdeplot(wasi_data['Time'], label='WASI')
sns.kdeplot(native_data['Time'], label='Native')

# Annotate peaks
for peak in peaks1:
    plt.axvline(x=x1[peak], color='blue', linestyle='--', alpha=0.7)
    plt.text(x1[peak] + 50, kde1(x1[peak]), f'{x1[peak]:.2f}', color='blue', fontsize=9)

for peak in peaks2:
    plt.axvline(x=x2[peak], color='orange', linestyle='--', alpha=0.7)
    plt.text(x2[peak] + 50, kde2(x2[peak]), f'{x2[peak]:.2f}', color='orange', fontsize=9)

# Add titles and labels
# plt.title('Latency of reading data from Arduino using read-bulk')
plt.xlabel('Duration (microseconds)')
plt.ylabel('Density')
plt.legend()

# Show the plot
plt.show()