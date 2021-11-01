#include <iostream>
using namespace std;

class Car{
    private:
        string name;
        string color;
        double price;
        bool isBroken;
    public:
        Car(string name, string color, double price){
            Name: name;
            Color: color;
            Price: price;
            isBroken = false;
        };
        void getInfo(){

        };
        void crashCar(){
            cout<<name<<" crashed"<<endl;
            isBroken = true;
        };
        void repairCar(){
            cout<<name<<" repaired"<<endl;
            isBroken = false;
        };
        void move(){
            if(isBroken)
                cout<<name<<" is broken"<<endl;
            else 
                cout<<name<<" is driving"<<endl;
        }
};

int main()
{
    Car Ford("Ford", "red", 50000);

    ford.move();
    ford.crashcar();
    ford.move();
    ford.repair();
    ford.move();
    
    system("pause>0");
}



