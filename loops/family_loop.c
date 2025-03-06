// Zoe jimenez, Family Loop C

#include <stdio.h>


int main(void){
    char familiars[][20] = {"Ruben", "Matthew", "Leo", "Vincent", "Josephine"};
    int flength = sizeof(familiars)/sizeof(familiars[0]);

    int f;
    for(f=0;f<flength;f++){
    printf("Hello, %s, Welcome to CSP!\n", familiars[f]);
}
    
    return 0;
}