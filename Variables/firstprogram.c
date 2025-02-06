// Zoe jimenez, first program C
#include <stdio.h>

char name[33];
int age;


int main(void){
    printf("welcome, what is your name: \n");
    scanf("%s", name);
    printf("whats your age: \n");
   scanf("%d", age);
    printf("Hello %s! you are %f years old!\n", name, age);

    return 0;
}
