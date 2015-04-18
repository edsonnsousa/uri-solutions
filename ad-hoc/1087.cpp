/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Mar 24 2015
 * 1087 - Dama
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1087
 *
 * ad-hoc
 */

#include <iostream>
#include <cstdlib>

using namespace std;

bool is_here(int, int, int, int);
bool is_lin_col(int, int, int, int);
bool is_diag(int, int, int, int);

int main(){
    int x1, y1, x2, y2;

    while (true) {
        cin >> x1 >> y1 >> x2 >> y2;

        if (x1 == 0) break;

        if (is_here(x1, y1, x2, y2))
            cout << '0' << endl;
        else if (is_lin_col(x1, y1, x2, y2) or is_diag(x1, y1, x2, y2))
            cout << '1' << endl;
        else
            cout << '2' << endl;
    }

    return 0;
}

bool is_here(int x1, int y1, int x2, int y2) {
    return x1 == x2 and y1 == y2;
}

bool is_lin_col(int x1, int y1, int x2, int y2) {
    return x1 == x2 or y1 == y2;
}

bool is_diag(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) == abs(y1 - y2);
}
