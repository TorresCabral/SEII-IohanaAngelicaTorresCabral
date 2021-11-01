#include <iostream>
using namespace std;


float sum(float a, float b);
void introduceMe(string name, int age = 0);

int main()
{
    cout<<sum(2.2, 5)<<endl;
    cout<<sum(5.2, 3)<<endl;
    cout<<sum(4, 8)<<endl;

    introduceMe("Iohana");

    system("pause>0");
}

float sum(float a, float b)
{
    return a + b;
}

void introduceMe(string name, int age){
    cout <<"My name is " << name << endl;
    cout <<"I am " << age <<" years old" << endl;
}