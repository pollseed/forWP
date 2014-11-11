#include <iostream>
using namespace std;

/* prototype */
void fizzbuzz(void);

int main(void)
{
    fizzbuzz();
    
    // pointer test
    int test = 0;
    int *pointer = nullptr;
    cout << "&test:" << &test << endl;
    pointer = &test;
    cout << "pointer:" << pointer << endl;
    cout << "test:" << test << endl;
    *pointer = 10;
    cout << "test = *pointer:" << test << endl;
    
    return 0;
}

// fizzbuzz function
void fizzbuzz(void)
{
    for (int i = 0; i < 100; i++)
    {
        if (i == 0)
            continue;
        
        cout << i << ":";
        if (i % 3 == 0)
        {
            cout << "FIZZ";
        }
        if (i % 5 == 0)
        {
            cout << "BUZZ";
        }
        cout << endl;
    }
}
