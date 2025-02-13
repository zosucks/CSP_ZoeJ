// Zoe Jimenez, Name Decorator C


#include <stdio.h>
   


int main(void){
    char name[50];
    printf("Hello user this is a program to decorate your name\n");
    printf("What is your name?: \n");
    scanf("%s", name);
    
    char one[50] = (":):)");
    char three[50] = (":):)");

   
    strcat(one, name);
    printf("%s", one);
    strcat(one, three);
    printf("%s\n", three);

    //printf("%d", name);

    return 0;
}