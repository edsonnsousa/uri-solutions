/**
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Apr 18 2015
 * 1162 - Organizador de Vagoes
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1162
 *
 * sort
 */

#include <cstdio>

int main() {
    int i, j, nTestCases, nCarriages, nSwaps, aux;
    int carriages[50];

    scanf("%d", &nTestCases);
    while (nTestCases--) {
        scanf("%d", &nCarriages);
        
        for (i = 0 ; i < nCarriages ; i++)
            scanf("%d", &carriages[i]);

        nSwaps = 0;
        for (i = 0 ; i < nCarriages ; i++) {
            for (j = 0 ; j < nCarriages - 1 - i; j++) {
                if (carriages[j] > carriages[j + 1]) {
                    aux = carriages[j + 1];
                    carriages[j + 1] = carriages[j];
                    carriages[j] = aux;
                    nSwaps++;
                }
            }    
        }

        printf("Optimal train swapping takes %d swaps.\n", nSwaps);
    }

    return 0;    
}
