// Zoe jimenez, Silly sentences C

#include <stdio.h>
// empty string vairables for user words (min 3)
    char color[20];
    char state[35];
    float num;
    float num1;
    char color1[35];
    char shape[50];
    char shape1[50];




int main(void){
    // a type of introduction
    printf("Welcome to my program user! This is a silly sentences maker! \n");

    // ask user for words (print statment with a question, scanf to set to variable)
    printf("Please name one color: \n");
    scanf("%d", color);

    printf("Please name a SINGLE WORD state: \n");
    scanf("%d", state);

    printf("Please type in a solid number: \n");
    scanf("%s", num);

    printf("Please type in another solid number: \n");
    scanf("%s", num1);

    printf("Please type another a ONE WORD color: \n");
    scanf("%d", color1);

    printf("Please name a ONE WORD shape: \n");
    scanf("%d", shape);

    printf("Please name another ONE WORD shape: \n");
    scanf("%d", shape1);
    // make sure to tell user to put in only one word.

    //print out the story with the variables inserted
    printf("A %d spaceship landed in %d. Can you believe that %s aliens got off the ship! They had %d eyes and two %d ")
    // all in one print statement!!
    
    return 0;
}