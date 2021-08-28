#include <iostream>
#include <vector>
using std::vector;
using std::cout;
vector<int> v;

void AddOneToEach(vector<int> &v) 
{
    for (auto& i: v) {
        i++;
    }
}