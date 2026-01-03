#include <stdbool.h>
#include <math.h>

#define EPSILON 1e-6

bool solve(double* nums, int n) {
    if (n == 1) return fabs(nums[0] - 24.0) < EPSILON;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            double a = nums[i], b = nums[j];
            double next[6];
            int idx = 0;

            for (int k = 0; k < n; k++) {
                if (k != i && k != j) next[idx++] = nums[k];
            }

            double results[6] = {a + b, a - b, b - a, a * b};
            int rCount = 4;

            if (fabs(b) > EPSILON) results[rCount++] = a / b;
            if (fabs(a) > EPSILON) results[rCount++] = b / a;

            for (int r = 0; r < rCount; r++) {
                next[idx] = results[r];
                if (solve(next, idx + 1)) return true;
            }
        }
    }
    return false;
}

bool judgePoint24(int* cards, int cardsSize) {
    double nums[4];
    for (int i = 0; i < cardsSize; i++) nums[i] = (double)cards[i];
    return solve(nums, cardsSize);
}
