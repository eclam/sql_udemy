#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <string>

using namespace std;
class Node {
public:
    int data;
    Node *left, *right;
    Node(int d) {
        data = d;
        left = right = NULL;
    }
};
class Solution {
private:
    queue<Node*> q1;

public:
    Node* insert(Node* root, int data) {
        if (root == NULL) {
            return new Node(data);
        } else {
            Node* cur;
            if (data <= root->data) {
                cur        = insert(root->left, data);
                root->left = cur;
            } else {
                cur         = insert(root->right, data);
                root->right = cur;
            }
            return root;
        }
    }

    void levelOrder(Node* root) {
        // Write your code here
        queue<Node*> q1;
        q1.push(root);
        while (q1.size() > 0) {
            Node* temp = q1.front();
            cout << temp->data << " ";
            if (temp->left != NULL) {
                q1.push(temp->left);
            }
            if (temp->right != NULL) {
                q1.push(temp->right);
            }
            q1.pop();
        }
    }

};  // End of Solution
int main() {
    Solution myTree;
    Node* root = NULL;
    int T, data;
    cin >> T;
    while (T-- > 0) {
        cin >> data;
        root = myTree.insert(root, data);
    }
    myTree.levelOrder(root);
    return 0;
}