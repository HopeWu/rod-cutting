class Solution:
    def maximumProfit(self, n: int, prices: [int]) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return prices[0]
        _max = 0
        _len = len(prices)
        for i in range(1, n+1):
            if i < _len:
                _max = max(prices[i-1] + self.maximumProfit(n-i, prices), _max)
        return _max


A = [1, 3, 4, 5, 7, 9, 10, 11]
n = 8

solution = Solution()
print(solution.maximumProfit(8, A))
