// Selection sort

#include <iostream>
#include <climits>
using namespace std;
int main(){
  int n;
  cin>>n;
  int arr[n];
  for (int i = 0; i<n; i++){
    cin>>arr[i];
  }
  for (int j = 0; j<n-1; j++){
    for (int k = j+1; k<n; k++){
      if (arr[k]<arr[j]){
        int temp = arr[k];
        arr[k] = arr[j];
        arr[j] = temp;
      }
    }
  }
  for (int l = 0; l<n; l++){
    cout<<arr[l]<<' ';
}
}