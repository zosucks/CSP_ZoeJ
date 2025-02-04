// Zoe Jimenez, Variable notes C
#include <stdio.h>

char name[20] = "ZOE";
int age;
float pi;

int main(void){
    printf("welcome, what is your name: \n");
    scanf("%s", name);
    printf("whats your age: \n");
    scanf("%d", age);
    printf("Write out as much of pie as you know: \n");
    scanf("%f", pi);

    return 0;
}