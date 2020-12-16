// Insertion sort
// Chose an element and insert it at it's correct place by moving the previous sorted elements forward by one step until the element's place comes, then place the element.
#include <iostream>
using namespace std;

int main(){
  int n;
  cin>>n;
  int arr[n];
  for (int i=0; i<n; i++){
    cin>>arr[i];
  }
  for (int i=1; i<n; i++){
    int current = arr[i];
    int j = i-1;
    // Don't use a[i] in place of current below as a[j+1] will replace the value of a[i] after the first iteration.
      while (current < arr[j] && j>=0){
        arr[j+1] = arr[j];
        j--;
      }
      arr[j+1] = current;
    }
  for (int i=0; i<n; i++){
    cout<<arr[i];
}}