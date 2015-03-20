/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Feb 27 2015
 * 1099 - Soma de Impares Consecutivos II
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1099
 *
 * ad-hoc
 *
 */

#include <iostream>
 
int main(){
    int i, x, y, s, nTests;

    std::cin >> nTests;
    while(nTests--) {
        s = 0;
        std::cin >> x;
        std::cin >> y;
     
        if (x < y){
            for (i = x + 1; i < y; i++){
                if (i % 2 != 0) s += i;
            }
        } else {
            for (i = y + 1; i < x; i++){
                if (i % 2 != 0) s += i;
            }
        }
 
        std::cout << s << std::endl;
    }

    return 0;
}
