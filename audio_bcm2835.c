#include <bcm2835.h>

#define PIN RPI_GPIO_P1_07 // GPIO 4

int main(int argc, char *argv[]) {
    if(!bcm2835_init())
	return 1;

    int frequency     = 20000;
    double wavelength = 1 / frequency * 1000;
    double halfwave   = wavelength / 2;

    // Set the pin to be an output
    bcm2835_gpio_fsel(PIN, BCM2835_GPIO_FSEL_OUTP);

    while(1) { // Blink
	bcm2835_gpio_write(PIN, HIGH);
	delay(halfwave);
	bcm2835_gpio_write(PIN, LOW);
	delay(halfwave);
    }

    return 0;
}