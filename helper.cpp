#include<bits/stdc++.h>
using namespace std;

#define v vector<int>

void print(v &A){for(int a : A){cout<<a<<" ";}cout<<"\n";}

struct TreeNode {
    int val;
    TreeNode *left=NULL, *right=NULL;
public:
    TreeNode(int x){this->val=x;}
};

v tree2arr(TreeNode* root){
    v res;
    if(!root){return res;}
    queue<TreeNode*> q;
    q.push(root);
    while(!q.empty()){
        TreeNode* node=q.front(); q.pop();
        res.push_back(node ? node->val : -1);
        if(node){
            q.push(node->left);
            q.push(node->right);
        }
    }
    return res;
}

string vec2string(v &A){
    string s = "";
    for(int a : A){s += to_string(a)+' ';}
    return s;
}

void writeArray(vector<int> &A, string fname="dump.txt"){
    ofstream file(fname);
    file << vec2string(A);
    file.close();
}

void runUtil(v &A, string s, string pyf="../run.py"){
    writeArray(A, s);
    string cmd = "python3 " + pyf + " -f " + s;
    system(cmd.c_str());
}

void simulateTree(TreeNode* root){
    v arr = tree2arr(root);
    runUtil(arr, "new.txt");
}
