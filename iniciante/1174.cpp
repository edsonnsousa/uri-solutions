/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Mar 20 2015
 * 1174 - Selecao em Vetor I
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1174
 *
 * ad-hoc
 *
 */

#include <iostream>

using namespace std;

int main() {   
    double n;

    for (int i = 0 ; i < 100 ; i++) {
        cin >> n;
        if (n <= 10) {
            cout << "A[" << i << "] = " << n << endl;
        }
    }

    return 0;
}
