#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        unordered_map<Node*, Node*> old_to_new;

        Node* curr = head;

        while (curr) {
            old_to_new[curr] = new Node(curr->val);
            curr = curr->next;
        }

        curr = head;

        while (curr) {
            old_to_new[curr]->next = old_to_new[curr->next];
            old_to_new[curr]->random = old_to_new[curr->random];
            curr = curr->next;
        }

        return old_to_new[head];
    }
};

void printList(Node* head) {
    while (head) {
        cout << "Value: " << head->val;

        if (head->random)
            cout << ", Random: " << head->random->val;
        else
            cout << ", Random: NULL";

        cout << endl;

        head = head->next;
    }
}

int main() {
    int n;
    cin >> n;

    if (n == 0) return 0;

    vector<Node*> nodes(n);

    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        nodes[i] = new Node(val);
    }

    for (int i = 0; i < n - 1; i++) {
        nodes[i]->next = nodes[i + 1];
    }

    for (int i = 0; i < n; i++) {
        int randomIndex;
        cin >> randomIndex;

        if (randomIndex != -1)
            nodes[i]->random = nodes[randomIndex];
    }

    Node* head = nodes[0];

    Solution sol;
    Node* copiedHead = sol.copyRandomList(head);

    cout << "\nCopied List:\n";
    printList(copiedHead);

    return 0;
}