#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define v vector<int>
#define vv vector<v>
#define vvv vector<vv>
#define P pair<int, int>

struct TreeNode {
    int val;
    TreeNode *left=NULL, *right=NULL;
public:
    TreeNode(int x){this->val=x;}
};

vector<int> getVec(){
    int n; cin>>n;
    vector<int> A(n);
    for(int &a : A){cin >> a;}
    return A;
}
vector<int> getVec(int n){
    vector<int> A(n);
    for(int &a : A){cin >> a;}
    return A;
}
vector<string> getVecString(){
    int n; cin>>n;
    vector<string> A(n);
    for(string &a : A){cin >> a;}
    return A;
}
vv getVV(){
    int m, n; cin>>m>>n;
    vv A(m, v(n));
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cin >> A[i][j];
        }
    }
    return A;
}

void print(int n){cout<<n<<"\n";}
void print(string s){cout << s << "\n";}
void print(int A[], int n){for(int i=0; i<n; i++){cout<<A[i]<< " ";}cout<<"\n";}
void print(vector<int> &A, string end=" "){for(int a : A){cout<<a<<" ";}cout<<"\n";}
void print(vv &A){for(int i=0; i<A.size(); i++){print(A[i]);}}
void print(vvv &A){for(int i=0; i<A.size(); i++){print(A[i]); print("");}}

void print(vector<string> &A, string end=" "){for(string a : A){cout<<a<<end;}cout<<"\n";}



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

int main(){

    v A = getVec();
    cout << "Enter output filename : ";
    string s; cin>>s;

    writeArray(A, s);

    string cmd = "python3 ../run.py -f " + s;
    system(cmd.c_str());

    return 0;
}