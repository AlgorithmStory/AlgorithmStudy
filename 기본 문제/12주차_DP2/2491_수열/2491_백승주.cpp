#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;
int main()
{
    int cnt;
    string str;
    vector<int> sequence;

    cin >> cnt;
    string line;
    cin.ignore();
    getline(cin, line);
    stringstream ss(line);

    while (getline(ss, str, ' ')) {
        sequence.push_back(stoi(str));
    }

    if (sequence.size() == 1) {
        cout << "1" << endl;
        return 0;
    }
    vector<int> asc_stack;
    vector<int> dec_stack;
    asc_stack.push_back(sequence[0]);
    dec_stack.push_back(sequence[0]);
    int asc_max = 2;
    int dec_max = 2;
    for (int i = 1; i < sequence.size(); ++i) {
        int current = sequence[i];
        if (current < asc_stack.back()) {
            asc_max = asc_stack.size() > asc_max ? asc_stack.size() : asc_max;
            asc_stack.clear();
        }
        asc_stack.push_back(current);

        if (current > dec_stack.back()) {
            dec_max = dec_stack.size() > dec_max ? dec_stack.size() : dec_max;
            dec_stack.clear();
        }
        dec_stack.push_back(current);
    }
    asc_max = asc_stack.size() > asc_max ? asc_stack.size() : asc_max;
    dec_max = dec_stack.size() > dec_max ? dec_stack.size() : dec_max;

    int max = asc_max > dec_max ? asc_max : dec_max;
    cout << max << endl;
    return 0;
}