/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Mar 18 2015
 * 1149 - Somando Inteiros Consecutivos
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1149
 *
 * ad-hoc
 */

#include <iostream>

using namespace std;

int main(){
    int a, n;

    cin >> a;
    while (true) {
        cin >> n;
        if (n > 0)
            break;
    }

    cout << (a + (a + n - 1)) * n / 2 << endl;

    return 0;
}
