#include <stdio.h>

char name[] = "ZOE";
int age = 14;
float pi = 3.14;

int main(void){
    printf("Hello i am %s. i am %d years old. And i like the number %f.\n", name, age, pi);
    printf("%d\n", age);
    printf("%f\n", pi);
    return 0;
}