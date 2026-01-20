char** getLongestSubsequence(char** words, int wordsSize, int* groups, int groupsSize, int* returnSize) {
    char** result = (char**)malloc(sizeof(char*) * wordsSize);
    int resIdx = 0, prevGroup = -1;
    for (int i = 0; i < wordsSize; ++i) {
        if (groups[i] != prevGroup) {
            result[resIdx++] = words[i];
            prevGroup = groups[i];
        }
    }
    *returnSize = resIdx;
    return result;
}