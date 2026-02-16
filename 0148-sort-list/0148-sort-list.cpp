/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        // Step 4: Base Case
        if (head == nullptr || head->next == nullptr) return head;

        // Step 2: Divide the problem into subproblems.
        // of size floor(n/2) and ceil(n/2)
        ListNode *head1 = head;
        ListNode *slow = head, *fast = head->next;

        while(fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next;
            slow = slow->next;
        }
        ListNode *head2 = slow->next;
        slow->next = nullptr; 

        // Step 1: Solve subproblems recursively
        head1 = sortList(head1);
        head2 = sortList(head2);

        // Step 3: Integrate the solution of subproblems.
        //  Into the solution of the problem. 
        ListNode *newHead = nullptr;
        ListNode *tail = nullptr;
        while(head1 != nullptr || head2 != nullptr) {
            ListNode *temp;
            if(head1 != nullptr && (head2 == nullptr || head1->val <= head2->val)) {
                temp = head1;
                head1 = head1->next;
            } else {
                temp = head2;
                head2 = head2->next;
            }

            if (newHead == nullptr) {
                newHead = temp;
                tail = temp;
            } else {
                tail->next = temp;
                tail = tail->next;
            }
        }

        if (tail) tail->next = nullptr;

        return newHead; 
    }
};