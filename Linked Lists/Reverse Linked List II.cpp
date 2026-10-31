#include <iostream>
using namespace std;

// Linked List Node
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == nullptr || left == right) {
            return head;
        }

        ListNode dummy(0);
        dummy.next = head;

        ListNode* prev = &dummy;

        for (int i = 0; i < left - 1; i++) {
            prev = prev->next;
        }

        ListNode* curr = prev->next;

        for (int i = 0; i < right - left; i++) {
            ListNode* temp = curr->next;

            curr->next = temp->next;
            temp->next = prev->next;
            prev->next = temp;
        }

        return dummy.next;
    }
};

// Print Linked List
void printList(ListNode* head) {
    while (head != nullptr) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

// Main part
int main() {
    // Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    int left = 2;
    int right = 4;

    Solution obj;

    cout << "Original List: ";
    printList(head);

    head = obj.reverseBetween(head, left, right);

    cout << "Reversed List: ";
    printList(head);

    return 0;
}