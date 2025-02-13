// Zoe Jimenez, Name Decorator C


#include <stdio.h>
    char name;


int main(void){
    printf("Hello user this is a program to decorate your name\n");
    printf("What is your name?: \n");
    scanf("%s", name);

    char one[] = (":):)");
    char three[] = (":):)");

   
    strcat(one, name);
    printf("%s", one);
    strcat(one, three);
    print("%s", three);

    printf("%s", name);

    return 0;
}