class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) return false;
        int i = 0;
        for(i = 0; i < matrix.size() - 1; i++) {
            if(target >= matrix[i][0] && target < matrix[i+1][0]) {
                break;
            }
        }

        if(target >= matrix[matrix.size() - 1][0]) i = matrix.size() - 1;

        int low = 0, high = matrix[0].size() - 1;
        while(low <= high) {
            int mid = low + (high - low) / 2;
            if(matrix[i][mid] == target) return true;
            else if(matrix[i][mid] < target) low = mid + 1;
            else high = mid - 1;
        }
        return false;
    }
};