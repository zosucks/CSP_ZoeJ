// Zoe Jimenez, Variables C
#include <stdio.h>

char name[] = "Zoe";
int number1 = 6;
float number2 = 753;
char breakfast[] = "cereal";
char school[] = "UCAS";
int year = 2025;
char eyecolor[] = "Brown";
int age = 14;
char favsub[] = "Math";

int main(void){
    printf("Hello i am %s. i like the number %d. And the number %f. Today i had %s at %s \n", name, number1, number2, breakfast, school);
    printf("I go to this school during the year %d, my eyes are %s while my age is %d \n", year, eyecolor, age);
    printf("My favorite subject in school is %s \n", favsub);
    printf("%d\n", number1);
    printf("%f\n", number2);
    return 0;
}


 