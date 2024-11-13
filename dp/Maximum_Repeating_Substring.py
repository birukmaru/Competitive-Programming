class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        dp = [0] * n
        max_repeat = 0
        
        # Iterate over the sequence starting from the position where word could fit
        for i in range(m - 1, n):
            if sequence[i - m + 1:i + 1] == word:
                # If we can extend a previous repeating substring
                if i - m >= 0:
                    dp[i] = dp[i - m] + 1
                else:
                    dp[i] = 1
                # Update the maximum repeat count
                max_repeat = max(max_repeat, dp[i])
        
        return max_repeat
