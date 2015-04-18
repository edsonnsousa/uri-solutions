/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Mar 24 2015
 * 1216 - Getline One
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1216
 *
 * ad-hoc
 */

#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(){
    int dist = 0, new_dist, count = 0;
    char newline;
    string name;

    while (getline(cin, name)) {
        cin >> new_dist >> noskipws >> newline;
        dist += new_dist;
        count++;
    }

    printf("%.1lf\n", dist / float(count));

    return 0;
}
