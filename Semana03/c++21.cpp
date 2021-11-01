#include <iostream>
using namespace std;

class Car{
    string name;
    string color;
    double price;
};

int main()
{
    Car myCar;
    myCar.name = "Ford";
    myCar.color = "red";
    myCar.price = 50000; 

    cout<<"Name: "<<myCar.name<<endl;
    cout<<"Color: "<<myCar.color<<endl;
    cout<<"Price: "<<myCar.price<<"$"<<endl;
    
    system("pause>0");
}



