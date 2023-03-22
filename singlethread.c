#include <iostream>		// Include all needed libraries here
#include <pigpio.h>

int main()
{
gpioSetMode(2, PI_OUTPUT);
gpioSetMode(3, PI_OUTPUT);

int frequency = 1000000; // Hz
double wavelength = 1/frequency; // Hz
double halfwave = wavelength/2;

// Main program loop
while(1)
{
	// Toggle the LED
	gpioWrite(2, 1);
	gpioWrite(3, 1);
    sleep_for(halfwave);

	gpioWrite(2, 0);
	gpioWrite(3, 0);
    sleep_for(halfwave);

}

	return 0;
}