#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    stack<int> s;
    stack<int> maxs;
    maxs.push(0);  // Initialize with 0
    int n;
    int val;
    cin >> n;
    while(n--)
    {
        int idx;
        cin >> idx;
        if(idx == 1)
        {
            cin >> val;
            if(val >= maxs.top())
            {
                maxs.push(val);
            }
            else
            {
                s.push(val);
            }
        }
        else if(idx == 2)
        {
             if(s.top() == maxs.top())
             {
                 maxs.pop();
             }
             else
             {
                 s.pop();
             }
         }
        else if(idx == 3)
        {
         cout << maxs.top() << endl;
        }

    }
    return 0;
}
