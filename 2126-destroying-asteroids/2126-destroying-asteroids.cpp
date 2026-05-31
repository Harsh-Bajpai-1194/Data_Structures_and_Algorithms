class Solution {
public:
    bool asteroidsDestroyed(long int mass, vector<int>& asteroids) {
        sort(asteroids.begin(),asteroids.end());
        for (int i=0; i<asteroids.size(); i++)
        {
            if (mass<asteroids[i]) return false;
            else mass+=asteroids[i];
        }
        return true;
    }
};