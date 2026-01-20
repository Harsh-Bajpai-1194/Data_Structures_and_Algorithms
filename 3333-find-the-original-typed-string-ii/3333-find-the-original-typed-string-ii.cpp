class Solution {
 public:
  int possibleStringCount(string word, int k) {
    const vector<int> groups = getConsecutiveLetters(word);
    const int totalCombinations =
        accumulate(groups.begin(), groups.end(), 1LL,
                   [](long long acc, int group) { return acc * group % kMod; });

    if (k <= groups.size())
      return totalCombinations;

    vector<int> dp(k);
    dp[0] = 1;

    for (int group : groups) {
      vector<int> newDp(k);
      long long windowSum = 0;
      for (int j = 0; j < k; ++j) {
        newDp[j] = (newDp[j] + windowSum) % kMod;
        windowSum = (windowSum + dp[j]) % kMod;
        if (j >= group)
          windowSum = (windowSum - dp[j - group] + kMod) % kMod;
      }
      dp = std::move(newDp);
    }

    int invalidCombinations =
        accumulate(dp.begin(), dp.end(), 0,
                   [](int acc, int count) { return (acc + count) % kMod; });

    return (totalCombinations - invalidCombinations + kMod) % kMod;
  }

 private:
  static constexpr int kMod = 1'000'000'007;

  vector<int> getConsecutiveLetters(const string& word) {
    vector<int> groups;
    int group = 1;
    for (int i = 1; i < word.length(); ++i) {
      if (word[i] == word[i - 1])
        ++group;
      else {
        groups.push_back(group);
        group = 1;
      }
    }
    groups.push_back(group);
    return groups;
  }
};
