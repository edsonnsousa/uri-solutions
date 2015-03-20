/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Mar 20 2015
 * 1180 - Menor e Posicao
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1180
 *
 * ad-hoc
 *
 */

#include <iostream>

using namespace std;

int main() {   
    int len, num, lower, idx;

    cin >> len;
    cin >> lower;
    idx = 0;
    for (int i = 1 ; i < len ; i++) {
        cin >> num;
        if (num < lower) {
            lower = num;
            idx = i;
        }
    }

    cout << "Menor valor: " << lower << endl;
    cout << "Posicao: " << idx << endl;

    return 0;
}
