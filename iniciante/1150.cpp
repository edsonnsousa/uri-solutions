/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Mar 18 2015
 * 1150 - Ultrapassando Z
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1150
 *
 * ad-hoc
 */

#include <iostream>

using namespace std;

bool sum_is_bigger(int, int, int);

int main(){
    int x, z;

    cin >> x;
    while (true) {
        cin >> z;
        if (z > x)
            break;
    }

    for (int i = 2 ; ; i++) {
        if (sum_is_bigger(x, z, i)) {
            cout << i << endl;
            break;
        }
    }

    return 0;
}

bool sum_is_bigger(int x, int z, int i) {
    return ((x + (x + i - 1)) * i / 2) > z;
}
