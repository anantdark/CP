#include<bits/stdc++.h>
#include<cmath>
#include<climits>
using namespace std;
#define li long long
int main(){
    li n;
    cin >> n;
    cout << n << " ";
    while(n>1){
        if (n%2!=0){
            n = (n*3)+1;
            cout << n << " ";
        }
        else{
            n /= 2;
            cout << n << " ";
        }
    }
}