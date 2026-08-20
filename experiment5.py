def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a DP table initialized with zeros
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1  # Characters match
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])  # Choose max

    return table[m][n]

# Example usage:
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS:", lcs(X, Y))  # Output: 4 ("GTAB")