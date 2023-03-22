#include <iostream>		// Include all needed libraries here
#include <wiringPi.h>

using namespace std;		// No need to keep using “std”

int main()
{
wiringPiSetup();			// Setup the library
pinMode(2, OUTPUT);		// Configure GPIO0 as an output

frequency = 1_000_000 // Hz
wavelength = 1/frequency // Hz
halfwave = wavelength/2

// Main program loop
while(1)
{
	// Toggle the LED
	digitalWrite(2, 1);
    delay(halfwave);
	digitalWrite(2, 0);
    delay(halfwave);
}

	return 0;
}