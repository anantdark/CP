// Print max number at ith index
#include <iostream>
#include<climits>
using namespace std;

int main(){
  int n;
  cin>>n; 
  int ans[n];
  for (int i=0; i<n; i++){
    cin>>ans[i];
  }
  int max=INT_MIN;
  cout<<max;
  for (int i=0; i<n; i++){
    if (ans[i]>max){
      cout<<ans[i]<<endl;
      max=ans[i];
    }
    else{
      cout<<max<<endl;
    }
  }
}