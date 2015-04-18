/*
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Apr 6 2015
 * 1089 - Loop Musical
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1089
 *
 * ad-hoc
 */

#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n, h, peaks;
    vector <int> music;

    while (true) {
        cin >> n;

        if (n == 0) break;

        music.clear();
        for (int i = 0 ; i < n ; i++) {
            cin >> h;
            music.push_back(h);
        }

        peaks = 0;
        if (music[n - 1] > music[0] and music[1] > music[0])
            peaks++;
        else if (music[n - 1] < music[0] and music[1] < music[0])
            peaks++;
        
        if (music[n - 2] > music[n - 1] and music[0] > music[n - 1])
            peaks++;
        else if (music[n - 2] < music[n - 1] and music[0] < music[n - 1])
            peaks++;
        
        for (int i = 1 ; i < n - 1; i++) {
            if (music[i - 1] > music[i] and music[i + 1] > music[i])
                peaks++;
            else if (music[i - 1] < music[i] and music[i + 1] < music[i])
                peaks++;
        }    

        cout << peaks << endl;
    }

    return 0;
}
