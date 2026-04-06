# Plots graphs of the results of the algorithm
import csv
import matplotlib.pyplot as plt
import os

csv_file = 'results/runtime.csv'
png_file = 'graph/runtime_graph.png'

os.makedirs('graph', exist_ok=True)
size, time = [], []

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        size.append(int(row[1]))  # len(A)
        time.append(float(row[3]))  # Runtime

plt.scatter(size, time)
plt.plot(size, time)
plt.xlabel('Size of Sequences')
plt.ylabel('Runtime (seconds)')
plt.title('HVLCS Runtime vs Input Size')
plt.savefig(png_file)