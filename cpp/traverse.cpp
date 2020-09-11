#include<bits/stdc++.h>
using namespace std;

#define v vector<int>

vector<int> getVec(){
    int n; cin>>n;
    vector<int> A(n);
    for(int &a : A){cin >> a;}
    return A;
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

void run(v &A, string &s){
    writeArray(A, s);
    string cmd = "python3 ../run.py -f " + s;
    system(cmd.c_str());
}

int main(){

    v A = getVec();
    cout << "Enter output filename : ";
    string s; cin>>s;

    run(A, s);

    return 0;
}