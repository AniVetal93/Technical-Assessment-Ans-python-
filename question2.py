# Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert the minimum number of characters from/in str1 to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted at some another point.

def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    # Create a 2D array to store lengths of longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def min_deletions_and_insertions(str1, str2):
    lcs_length = longest_common_subsequence(str1, str2)
    
    # Calculate deletions and insertions
    deletions = len(str1) - lcs_length
    insertions = len(str2) - lcs_length
    
    return deletions, insertions

# Example input
str1 = "heap"
str2 = "pea"
deletions, insertions = min_deletions_and_insertions(str1, str2)

# Output the result
print(f"Minimum Deletion = {deletions} and Minimum Insertion = {insertions}")
