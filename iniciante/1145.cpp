/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Mar 17 2015
 * 1145 - Sequencia Logica 2
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1145
 *
 * ad-hoc
 */

#include <iostream>

using namespace std;

int main(){
    int x, y;
    
    cin >> x >> y;
    
    for(int i = 1; i <= y; i++){
        if(i % x == 0)
            cout << i << "\n";
        else
            cout << i << " ";
    }

    return 0;
}
