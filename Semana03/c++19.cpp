#include <iostream>
using namespace std;

void celebrateBirthday(int* age);

int main()
{
    int myAge = 25;
    cout<<"Before function "<<myAge <<endl;
    celebrateBirthday(&myAge);
    cout<<"After function age: "<<myAge <<endl;

    system("pause>0");
}

void celebrateBirthday(int* age){
    (*age)++;
    cout<<"Yeeeey, celebrated "<< *age <<" birthday"<<endl;
}

