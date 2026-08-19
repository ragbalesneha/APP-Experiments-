# Function 1: Top-Down Dynamic Programming (Memoization)
def fib_memoization(n: int, memo: dict = None) -> int:
    """Computes the nth Fibonacci number using Top-Down Dynamic Programming (Memoization).

    Time Complexity: O(n) | Space Complexity: O(n)
    """
    if memo is None:
        memo = {}

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Return cached result if available
    if n in memo:
        return memo[n]

    # Recursive call with caching
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]


# Function 2: Bottom-Up Dynamic Programming (Tabulation)
def fib_tabulation(n: int) -> int:
    """Computes the nth Fibonacci number using Bottom-Up Dynamic Programming (Tabulation).

    Time Complexity: O(n) | Space Complexity: O(n)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Initialize lookup table
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    # Fill table iteratively
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Function 3: Space-Optimized Iterative Approach
def fib_space_optimized(n: int) -> int:
    """Computes the nth Fibonacci number with optimal memory usage.

    Time Complexity: O(n) | Space Complexity: O(1)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


# ==========================================
# Execution & Verification
# ==========================================
if __name__ == "__main__":
    n = 10

    print(f"Calculating the {n}th Fibonacci number:\n" + "-" * 38)
    print(f"1. Memoization (Top-Down) : {fib_memoization(n)}")
    print(f"2. Tabulation (Bottom-Up) : {fib_tabulation(n)}")
    print(f"3. Space-Optimized        : {fib_space_optimized(n)}")