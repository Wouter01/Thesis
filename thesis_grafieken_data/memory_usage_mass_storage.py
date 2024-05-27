import matplotlib.pyplot as plt

# Set to True to generate other graph.
only_filetree_reading = False

if only_filetree_reading:
    file = 'mass_storage/memory_results_wasi_tree.txt'
    file2 = 'mass_storage/memory_results_native_tree.txt'
else:
    file = 'mass_storage/memory_results_wasi.txt'
    file2 = 'mass_storage/memory_results_native.txt'

with open(file, 'r') as file:
    data = [int(usage) / 1_000_000 for usage in file]

with open(file2, 'r') as file:
    data2 = [int(usage) / 1_000_000 for usage in file]

print(max(data), max(data2))

fst = data[0]

plt.plot(data, label="WASI")
plt.plot(data2, label="Native")

if only_filetree_reading:
    correction = [i - fst for i in data]
    plt.plot(correction, label="WASI, corrected")

plt.xlabel('Time Steps (1ms interval)')
plt.ylabel('Memory Usage (Megabytes)')
plt.legend()
plt.grid(True)
# plt.ylim(0, max(max(data), max * 1.1)
plt.show()