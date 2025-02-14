// Zoe jimenez, Silly sentences C

#include <stdio.h>
// empty string vairables for user words (min 3)
    char color[20];
    char state[20];
    float num;
    float num1;
    char color1[20];
    char shape[20];
    char shape1[20];




int main(void){
    // a type of introduction
    printf("Welcome to my program user! This is a silly sentences maker! \n");

    // ask user for words (print statment with a question, scanf to set to variable)
    printf("Please name one color: \n");
    scanf("%s", &color);

    printf("Please name a SINGLE WORD state: \n");
    scanf("%s", &state);

    printf("Please type in a solid number: \n");
    scanf("%d", &num);

    printf("Please type in another solid number: \n");
    scanf("%d", &num1);

    printf("Please type another a ONE WORD color: \n");
    scanf("%s", &color1);

    printf("Please name a ONE WORD shape: \n");
    scanf("%s", &shape);

    printf("Please name another ONE WORD shape: \n");
    scanf("%s", &shape1);
    // make sure to tell user to put in only one word.

    //print out the story with the variables inserted
    printf("A %s spaceship landed in %s. Can you believe that %d aliens got off the ship! They had %d eyes and two %s mouths! They had %s heads and %s noses! \n", color, state, num, num1, color1, shape, shape1);
    // all in one print statement!!
    
    return 0;
}