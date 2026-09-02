# Bottom-up (Iterative)
def knapsack_bottom_up(W, wt, val, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Top-down (Recursive with Memoization)
def knapsack_top_down(W, wt, val, n, memo=None):
    if memo is None:
        memo = {}

    if n == 0 or W == 0:
        return 0

    if (n, W) in memo:
        return memo[(n, W)]

    if wt[n - 1] <= W:
        include = val[n - 1] + knapsack_top_down(
            W - wt[n - 1], wt, val, n - 1, memo
        )
        exclude = knapsack_top_down(
            W, wt, val, n - 1, memo
        )

        memo[(n, W)] = max(include, exclude)
    else:
        memo[(n, W)] = knapsack_top_down(
            W, wt, val, n - 1, memo
        )

    return memo[(n, W)]


# Input
W = 50
wt = [10, 20, 30]
val = [60, 100, 120]
n = len(wt)

# Function calls
result_bottom_up = knapsack_bottom_up(W, wt, val, n)
result_top_down = knapsack_top_down(W, wt, val, n)

# Output
print("Bottom-up Knapsack Result:", result_bottom_up)
print("Top-down Knapsack Result:", result_top_down)