#include<bits/stdc++.h>
#include "../helper.cpp"
using namespace std;

int main(){
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);
    root->right->left->right = new TreeNode(8);
    root->right->left->right->left = new TreeNode(10);

    simulateTree(root);

    return 0;
}