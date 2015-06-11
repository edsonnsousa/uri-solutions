/**
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Apr 18 2015
 * 1062 - Trilhos
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1062
 *
 * stack
 */

#include <cstdio>
#include <stack>

using namespace std;

int main() {
    int len, wagon, caught;

    while (true) {
        scanf("%d", &len);
            
        if (len == 0) break;

        while (true) {
            scanf("%d", &wagon);

            if (wagon == 0) break;
            
            stack <int> estacao;
            caught = 1;

            for(int i = 1 ; i <= len ; i++) {
                estacao.push(i);
                while (!estacao.empty() and estacao.top() == wagon) {
                    estacao.pop();
                    if (caught < len) {
                        scanf("%d", &wagon);
                        caught++;
                    }
                }
            }

            if (estacao.empty() and caught == len) 
                printf("Yes\n");
            else 
                printf("No\n");

            while (caught < len) {
                scanf("%d", &wagon);
                caught++;
            }
        }

        printf("\n");
    }
    
    return 0;    
}
