/**
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Apr 27 2015
 * 1424 - Problema Facil de Rujia Liu?
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1424
 *
 * map
 */

#include <cstdio>
#include <vector>
#include <map>

using namespace std;

int main() {
    int n, m, k, v, num;
    map <int, vector <int> > serie;

    while (scanf("%d %d", &n, &m) != EOF) {
        serie.clear();
        for (int i = 0 ; i < n ; i++) {
            scanf("%d", &num);
            serie[num].push_back(i);
        }

        for (int i = 0 ; i < m ; i++) {
            scanf("%d %d", &k, &v);
            if (serie[v].size() < k)
                printf("0\n");    
            else
                printf("%d\n", serie[v][k - 1] + 1);
        }
    }

    return 0;    
}
