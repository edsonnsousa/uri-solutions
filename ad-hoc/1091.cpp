/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Apr 6 2015
 * 1091 - Divisao da Nlogonia
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1091
 *
 * ad-hoc
 */

#include <iostream>

using namespace std;

int main(){
    int k, x0, y0, x, y;

    while (true) {
        cin >> k;

        if (k == 0) break;

        cin >> x0 >> y0;
        for (int i = 0 ; i < k ; i++) {
            cin >> x >> y;
            if (x == x0 or y == y0)
                cout << "divisa" << endl;
            else if (x > x0 and y > y0)
                cout << "NE" << endl;
            else if (x < x0 and y > y0)
                cout << "NO" << endl;
            else if (x < x0 and y < y0)
                cout << "SO" << endl;
            else
                cout << "SE" << endl;
        }

    }

    return 0;
}
