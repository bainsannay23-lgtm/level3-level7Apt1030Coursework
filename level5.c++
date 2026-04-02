#include <iostream>
using namespace std;

double calculateFare(double distance) {
    double baseFare = 200.0;
    double costPerKm = 50.0;
    return baseFare + (costPerKm * distance);
}

int main() {
    cout << "Total Fare: " << calculateFare(10.5) << " KES" << endl;
    return 0;
}
