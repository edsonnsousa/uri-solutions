/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Mar 24 2015
 * 1103 - Alarme Despertador
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1103
 *
 * ad-hoc
 */

#include <iostream>

using namespace std;

int main(){
    int h1, m1, h2, m2;
    int sleep, wakeup;

    while (true) {
        cin >> h1 >> m1 >> h2 >> m2;

        if (h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0) break;

        sleep  = h1 * 60 + m1;
        wakeup = h2 * 60 + m2;
       
        if (wakeup >= sleep)
            cout << wakeup - sleep << endl;
        else
            cout << (24 * 60 - sleep) + wakeup << endl;
    }

    return 0;
}
