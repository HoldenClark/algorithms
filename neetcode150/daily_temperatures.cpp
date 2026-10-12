#include <iostream>
#include <vector>
#include <stack>

std::vector<int> test {30,38,30,36,35,40,28};

class Solution {
    public:
        std::vector<int> dailyTemperatures(std::vector<int>& temperatures) {
            // init our return
            const int iSize = temperatures.size();
            std::vector<int> res(iSize, 0);
    
            // used for calculating the day diff and which index to place at in the res
            std::stack<int> myStack = {};
    
            // loop through values in our input array, O(n)
            for (int i = 0; i < iSize; ++i) {
                while (!myStack.empty() && temperatures[i] > temperatures[myStack.top()]) {
                    int index = myStack.top(); // index of temp at top of stack for comparison
                    int diff = i - myStack.top(); // diff calculated from top of stack index and current index
                    res.at(index) = diff; // placing diff at index of temp stored on top of stack
                    myStack.pop(); // pop calculated temp index and move on
                }
                myStack.push(i);
            }
            return res;
        }
};

int main() {
    Solution solution;
    
    std::vector<int> test_result = solution.dailyTemperatures(test);
    
    for (int i {0}; i < test_result.size(); ++i) {
        std::cout << test_result[i] << std::endl;
    }
}
