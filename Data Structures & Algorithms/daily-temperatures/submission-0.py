class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):

            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                # Calculate the number of days to wait
                ans[i] = -(i - stack[-1])

            # Push the current index
            stack.append(i)

        return ans