#include <sys/time.h>
#include <bcm2835.h>

#define PIN RPI_GPIO_P1_07 // GPIO 4


void sleep_micro(uint32_t micro_seconds) {
    struct timeval start, end;
    gettimeofday(&start, NULL);
 
    for (int i = 0; i <1e5 ; i++) {
    }
 
    gettimeofday(&end, NULL);
    printf("Time taken to count to 10^5 is : %ld micro seconds\n",
      ((end.tv_sec * 1000000 + end.tv_usec) -
      (start.tv_sec * 1000000 + start.tv_usec)));

}


int main(int argc, char *argv[]) {

    if(!bcm2835_init())
	return 1;

    uint32_t microseconds = 0;
    uint64_t time = timeval.tv
    uint64_t 
    // Set the pin to be an output
    bcm2835_gpio_fsel(PIN, BCM2835_GPIO_FSEL_OUTP);

    

    

    while(1) { // Blink
	bcm2835_gpio_write(PIN, HIGH);
	//delay(500);
	bcm2835_gpio_write(PIN, LOW);
	//delay(500);
    }

    return 0;
}