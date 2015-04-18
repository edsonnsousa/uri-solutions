/**
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Apr 7 2015
 * 1031 - Crise de Energia
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1031
 *
 * ad-hoc
 */

#include <iostream>

using namespace std;

int josephus(int, int);

int main() {
    int num, step, result;

    while (1) {
        cin >> num;

        if (num == 0) break;

        for (step = 1 ; ; step++) {
            result = josephus(num - 1, step) + 2; 
            if (result == 13) {
                cout << step << endl;
                break;        
            }
        }
    }

    return 0;
}

int josephus(int n, int k) {
    if (n == 1)
        return 0;
    return ((josephus(n - 1, k) + k) % n);
}
