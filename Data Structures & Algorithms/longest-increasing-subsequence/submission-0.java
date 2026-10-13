class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int maxLen = 0;
        for (int i = 1 ; i<nums.length ; i ++){
            for (int j = 0 ; j< i - 1 ; j++){
                if (nums[i] > nums [j]){
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
        }
        for (int u=0 ; u<dp.length;u++){
            maxLen = Math.max(maxLen, dp [u] +1);
        }
        return maxLen;

    }
}
