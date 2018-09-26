#include <vector>
#include <iostream>
#include <stdio.h>
using namespace std;

int numberAlreadyFound(int number, vector<int> array) {
    for(int i = 0; i < array.size(); i++) {
        if(array[i] == number) {
            return 1;
        }
    }
    return 0;
}

int numberOfPairs(vector<int> array, int k){
    vector<int> numbersFound;
    int pairs = 0;
    for(int i = 0;i < array.size();i++) {
        if(!numberAlreadyFound(array[i], numbersFound)){
            for(int n = i + 1;n < array.size();n++){
                if(array[i] + array[n] == k) {
                    pairs++;
                    numbersFound.push_back(array[i]);
                    numbersFound.push_back(array[n]);
                    // Stop looking for
                    n = array.size();
                }
            }
        }
    }
    return pairs;
}


int main (){
    vector<int> A({5,5,5,5,5,5,5,5,5,5});
    cout << numberOfPairs(A, 10) << '\n';
}