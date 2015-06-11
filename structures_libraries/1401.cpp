/**
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Apr 27 2015
 * 1401 - Gerando Permutacoes Ordenadas Rapidamente
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1401
 *
 * next_permutation
 */

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<char> split(const string &line);

int main() {
    int n;
    char c;
    string line;
    vector <char> to_permute;

    cin >> n;
    for (int i = 0 ; i < n ; i++) {
        cin >> line;
        to_permute = split(line);
    
        sort(to_permute.begin(), to_permute.end());
        do {
            cout << string(to_permute.begin(), to_permute.end()) << endl;    
        } while (next_permutation(to_permute.begin(), to_permute.end())) {
        cout << endl;
    }

    return 0;    
}

vector<char> split(const string &line) {
    vector <char> my_vector;
    stringstream ss(line);
    char var;
    
    while (ss >> var)
        my_vector.push_back(var);
    
    return my_vector;
}
