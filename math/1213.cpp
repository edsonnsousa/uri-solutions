/**
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Apr 15 2015
 * 1213 - Ones
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1213
 *
 * math
 */

#include <cstdio>

int howManyOnes(int num);

int main() {
    int num;
        
    while(scanf("%d", &num) != EOF)
        printf("%d\n", howManyOnes(num));

    return 0;
} 

int howManyOnes(int num) {
    long div = 1;
    int resto, count = 1;
    
    while (true) {
        if (div < num) {
            div = div*10 + 1;
            count++;
        } 
       
        resto = div % num;

        if (resto == 0)
            break;    
        else
            div = resto;    
    }

    return count;
}
