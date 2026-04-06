# Computes Highest Value Longest Common Sequence 
import sys 
import time

def parser(lines): # Parses input file and returns weights, A, and B
    ptr = 0
    k = int(lines[ptr].strip())
    ptr += 1

    weights = {}
    for _ in range(k):
        char, val = lines[ptr].split()
        weights[char] = int(val)
        ptr += 1

    A = lines[ptr].strip()
    ptr += 1
    B = lines[ptr].strip()
    ptr += 1

    return weights, A, B


def construct_dp(A, B, weights): # Constructs dp table for highest value longest common subsequence
    n, m = len(A), len(B)

    # Initialize dp table with 0s, dimensions (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1): 
        for j in range(m - 1, -1, -1):
            # If characters match, calculate target value by adding weight of character to value from next diagonal cell (dp[i+1][j+1])
            if A[i] == B[j]:
                target = dp[i][j] = dp[i + 1][j + 1] + weights[A[i]]
                skip_a = dp[i + 1][j]
                skip_b = dp[i][j + 1]
                dp[i][j] = max(target, skip_a, skip_b)
            # If characters don't match,take max value from skipping character in A (dp[i+1][j]) or skipping character in B (dp[i][j+1])
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp

def callback(A, B, weights, dp): # Backtracking through dp table to construct highest value longest common subsequence
    i = 0
    j = 0
    subseq = []
    while i < len(A) and j < len(B):

        if A[i] == B[j] and dp[i][j] == dp[i + 1][j + 1] + weights[A[i]]: # if chars match, append char to subsequence
            subseq.append(A[i])
            i += 1
            j += 1
        
        elif dp[i][j] == dp[i + 1][j]: # Skip A
            i += 1

        else: # Skip B
            j += 1

    return "".join(subseq)
    

def solve(lines): # Main function to solve problem, calls parser, construct_dp, and callback functions
    weights, A, B = parser(lines)
    dp = construct_dp(A, B, weights)
    subseq = callback(A, B, weights, dp)
    return dp[0][0], subseq

def main(): # Reads input file, calls solve function, and prints results along with time taken
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
    
    value, subseq = solve(lines)
    
    print(f"Value: {value}")
    print(f"Subsequence: {subseq}")
    
if __name__ == "__main__":
    main()