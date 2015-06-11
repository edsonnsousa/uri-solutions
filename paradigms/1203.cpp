/**
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * May 28 2015
 * 1203 - Pontes de Sao Petersburgo
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1203
 *
 * pd
 */

#include <cstdio>

int main() {
    int r, k, reg1, reg2;

    while (scanf("%d %d", &r, &k) != EOF) {
        int region_degree[110] = {0};
        for (int i = 0 ; i < k ; i++) {
            scanf("%d %d", &reg1, &reg2);
            region_degree[reg1]++;
            region_degree[reg2]++;
        }

        bool isOK[5100] = {false};
        isOK[0] = true;

        for (int i = 1 ; i <= r ; i++) {
            for (int j = k ; j >= region_degree[i] ; j--) {
                if (isOK[j - region_degree[i]]) {
                    isOK[j] = true;    
                }    
            }
        }
        
        if (isOK[k])
            printf("S\n");    
        else
            printf("N\n");        
    }

    return 0;
}
