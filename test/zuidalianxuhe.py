def findmax(nums):
    dp = [0] * (len(nums)+1)
    s = 0
    for i in range(1,len(nums)+1):
        dp[i] = max(nums[i-1], dp[i-1]+nums[i-1])

    return max(dp)

res =findmax([1,2,-3,4,12,1,-20])