"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        cnt = 0
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])
            cnt += candies[i - 1]
        return cnt + candies[n - 1]

if __name__ == "__main__":
    solution = Solution()
    
    # # Example 1
    # ratings1 = [1,0,2]
    # result1 = solution.candy(ratings1)
    # print(f"Input: {ratings1}, Output: {result1}, Expected: 5")
    
    # # Example 2  
    ratings2 = [1,2,2]
    result2 = solution.candy(ratings2)
    print(f"Input: {ratings2}, Output: {result2}, Expected: 4")

    # ratings3 = [1,3,2,2,1]
    # result3 = solution.candy(ratings3)
    # print(f"Input: {ratings3}, Output: {result3}, Expected: 7")