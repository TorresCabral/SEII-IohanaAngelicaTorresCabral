#include <iostream>
using namespace std;

class Car{
    string name;
    string color;
    double price;

    Car(string name, string color, double price){
        Name: name;
        Color = color;
        Price = price;
    }
};

int main()
{
    Car myCar("Ford", "red", 50000);

    cout<<"Name: "<<myCar.name<<endl;
    cout<<"Color: "<<myCar.color<<endl;
    cout<<"Price: "<<myCar.price<<"$"<<endl;
    
    system("pause>0");
}



