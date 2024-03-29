#include <sys/time.h>
#include <stdio.h>


void sleep_micro(unsigned long int micro_seconds) {
    struct timeval start, end;
    gettimeofday(&start, NULL);
 

    do {
        gettimeofday(&end, NULL);
        if (
            (end.tv_sec * 1000000 + end.tv_usec) -
            (start.tv_sec * 1000000 + start.tv_usec) > micro_seconds) {
                break;
            }
    } while (1);

}
 
int main() {
    
    unsigned long int micros = 100;
    struct timeval before, after;
    gettimeofday(&before, NULL);
   
    for (int i = 0; i <1e2 ; i++) {
      sleep_micro(micros);
      gettimeofday(&after, NULL);
      printf("Time taken to count to 10^5 is : %ld micro seconds\n",
        ((before.tv_sec * 1000000 + before.tv_usec) -
        (before.tv_sec * 1000000 + before.tv_usec)));
    }
  
    return 0;
}  
  







