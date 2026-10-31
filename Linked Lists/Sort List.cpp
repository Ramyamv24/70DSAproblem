#include <iostream>
using namespace std;


struct ListNode {
    int val;
    ListNode* next;

    ListNode(int x) {
        val = x;
        next = nullptr;
    }
};

class Solution {
public:
    ListNode* sortList(ListNode* head) {

        if (!head || !head->next)
            return head;

        // Step 1: Find middle
        ListNode* slow = head;
        ListNode* fast = head->next;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Step 2: Divide into two lists
        ListNode* mid = slow->next;
        slow->next = nullptr;

        // Step 3: Sort both halves
        ListNode* left = sortList(head);
        ListNode* right = sortList(mid);

        // Step 4: Merge sorted lists
        return merge(left, right);
    }

    ListNode* merge(ListNode* list1, ListNode* list2) {

        ListNode dummy(0);
        ListNode* curr = &dummy;

        while (list1 && list2) {
            if (list1->val <= list2->val) {
                curr->next = list1;
                list1 = list1->next;
            }
            else {
                curr->next = list2;
                list2 = list2->next;
            }

            curr = curr->next;
        }

        curr->next = list1 ? list1 : list2;

        return dummy.next;
    }
};

// Function to print linked list
void printList(ListNode* head) {
    while (head != nullptr) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

// Main part
int main() {

    // Creating linked list: 4 -> 2 -> 1 -> 3 -> 5
    ListNode* head = new ListNode(4);
    head->next = new ListNode(2);
    head->next->next = new ListNode(1);
    head->next->next->next = new ListNode(3);
    head->next->next->next->next = new ListNode(5);

    Solution obj;

    cout << "Original List: ";
    printList(head);

    head = obj.sortList(head);

    cout << "Sorted List: ";
    printList(head);

    return 0;
}