class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length == 0)
        return;
        int temp[] = new int[nums.length];
        int m =0;
        for(int i =0;i< nums.length ;i++)
         {
            if(nums[i] != 0){
            temp[m] = nums[i];
            m++;
            }
         }
        
        
        for(int i=0; i< m ;i++)
        nums[i] = temp[i];

        for(int i = m; i < nums.length ;i++)
        nums[i] = 0;

        for(int i = 0; i < nums.length ;i++)
        System.out.print(nums[i]);

        


    }
}