// selection sort
#include <iostream>
using namespace std;

int main(){
  int n;
  cin>>n;
  int ans[n];
  for (int i=0; i<n; i++){
    cin>>ans[i];
  }
  for (int j = 0; j < n-1; j++){
    // Got segmentation fault as wrote j instead of k in the below loop, but the error segmentation fault doesn't help to point out the issue here.
    for (int k = j+1; j < n; k++){
      if ((ans[j] > ans[k])){
        int temp = ans[j];
        ans[j] = ans[k];
        ans[k] = temp;
      }
    }
  }
  for (int k = 0; k<n; k++){
    cout<<ans[k];
  }
}