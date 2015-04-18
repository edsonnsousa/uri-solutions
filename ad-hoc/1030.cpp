/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Apr 7 2015
 * 1030 - A Lenda de Flavious Josephus
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1030
 *
 * ad-hoc
 */

#include <iostream>
#include <cstdio>

using namespace std;

int josephus(int n, int k);

int main() {
    int nTests, n, k;

    cin >> nTests;
    for (int nt = 1 ; nt <= nTests ; nt++) {
        cin >> n >> k;
        printf("Case %d: %d\n", nt, josephus(n, k) + 1);
    }

    return 0;
}

int josephus(int n, int k) {
    if (n == 1)
        return 0;
    return (josephus(n - 1, k) + k) % n;
}
