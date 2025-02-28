// Zoe Jimenez, Time of Day C
#include <stdio.h>
#include <time.h>



int main(void){

    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    
    if(hour >= 18 && hour <= 22){
        printf("Good evening!");
    }else if(hour >= 12){
        printf("Good afternoon, have you eaten anything?");
    }else if(hour >= 6){
        printf("Goodmorning! Time to begin the day!");
    }else{
        printf("Get to bed what are you doing awake at this time?");
    }

    
    return 0;
}