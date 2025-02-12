// Zoe Jimenez, Name Decorator C


#include <stdio.h>
char name[55];
char one = ("###");
char three = ("###");

int main(void){
    printf("Hellow user this is a program to decorate your name\n");
    printf("What is your name?: \n");
    scanf("%d", name);


strcat(one, name);
strcat(one, three);


    return 0;
}