public class Solution {
    public bool IsArraySpecial(int[] nums) {
        if (nums.Length==1) return true;
        if (nums[0]%2==nums[1]%2) return false;
        for (int i=0; i<nums.Length-1; i++)
        {
            if (nums[i]%2==nums[i+1]%2) return false;
        }
        return true;
    }
}