# Creates files in results directory for series of tests in tests directory, and a CSV file with runtimes for each test.
import os
import csv
import time
import glob
from Sequence import solve

data_dir = "tests/test*.in"
results_file = "results/runtime.csv"
os.makedirs("results", exist_ok=True)

files = sorted(glob.glob(data_dir), key=os.path.getsize) 

with open(results_file, "w", newline="") as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(["Test File", "len(A)", "len(B)", "Runtime (seconds)"])

    # Process each test file
    for file in files:
        with open(file, "r") as f:
            lines = f.read().strip().splitlines()
        
        k = int(lines[0])
        A = lines[k + 1]
        B = lines[k + 2]

        start_time = time.time()
        val, subseq = solve(lines)
        runtime = time.time() - start_time
        
        # Write results to CSV file
        writer.writerow([file, len(A), len(B), runtime])
        #print results to console 
        print(f"Tested {file}: n = {len(A)}, m = {len(B)}, runtime = {runtime:.4f} seconds")
        #  Write results to output files
        with open(f"results/{os.path.basename(file).replace('.in', '.out')}", "w") as out_file:
            out_file.write(f"Value: {val}\nSubsequence: {subseq}\nRuntime: {runtime:.4f} seconds\n")

