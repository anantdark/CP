#include<bits/stdc++.h>
#include<cmath>
#include<climits>
using namespace std;
#define li long long
int main(){
    int n;
    cin >> n;
    int arr[n-1];
    int sum = 0;
    int finsum = (n*(n+1))/2;
    for (int i=1; i<n; i++){
        cin >> arr[i];
        sum += arr[i];
    }
    cout << finsum-sum << endl;
}