class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int o =0 ;
        for(int i =0 ; i< n ; i++ ){
            if(nums[i]==1)o++;
        }
        if(o!=0){
            return n-o;
        }
        int g = nums[0],in;
        for(int i =1 ; i< n ; i++ ){
            g = gcd(g,nums[i]);
            if(g==1){
                in = i;
                break;
            }
        }
        if(g!=1)return -1;
        int count =0;
        
        for(int i =0 ; i< n-1 ; i++ ){
            if(gcd(nums[i],nums[i+1]) == 1){
                o++;
                break;
            }
        }
        if(o!=0)return n;

        int c =0 ;
        g = nums[in];
        
        for(int i= in-1 ; i>=0 ; i--){
            g = gcd(nums[i],g);
            c++;
            if(g==1)break;
        }
        return n-1+c;
    }
};