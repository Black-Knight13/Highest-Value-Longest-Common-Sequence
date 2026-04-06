# Highest-Value-Longest-Common-Sequence
Jackson Turnbull 41914654

## How to Run

### Generate test data
```bash
python3 src/gen.py
```
Expected output:
```
Outputs files to tests directory
```

### Single file
```bash
python3 src/Sequence.py tests/test1.in
```

Expected output:
```
Value: <number>
Subsequence: <string>
```

### Run all tests
```bash
python3 src/test.py
```
Expected output:
```
Outputs files to results directory
```
### Plot runtimes
```bash
python3 src/plot.py
```
Expected output:
```
produces graph png in graph directory
```

## Assumptions
1. Input is plain txt file 
2. All weights positive ints
3. Characters in A & B present in weighted alphabet
4. Any optimal subsequence is acceptable

## Written Component
Found in pdf