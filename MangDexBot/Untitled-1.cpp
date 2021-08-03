//Jack Diver
#include <iostream>
using namespace std;

// Im using some of my code from the MPL question 70007 which is almost the same problem as this

int main() {
	double x;
	cout << "How many acres? ";
	cin >> x; 

	double acres = x * 43560;
	
	cout << x << " acres is equal to " << acres << " square feet." << endl;

}