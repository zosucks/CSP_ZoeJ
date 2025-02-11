// Zoe jimenez, String notes C
#include <stdio.h>
#include <string.h>

char subject[50];
char name[] = "Victoria";
char sentence[] = "The quick brown fox jumps over the lazy dog.";


int main(void){
    //printf("What class are you in?\n");
    //fgets(subject, sizeof(subject), stdin);
    //scanf("%s", subject);
    // scanf stops after one word
    //printf("You are in %s", subject);
    //name[0] = 'T';
    //name[1] = 'o';
    //name[2] = 'r';
   // name[3] = 'i';
//printf("%s", name);

//printf("%lu\n",sizeof(sentence));
// size of starts at 0 o you get one extra number
//printf("%d\n",strlen(sentence));

char one[] = "Hello ";
char two[] = "world!";
char three[] = "Welcome to my program. ";
printf("%s\n", one);
strcat(one, two);
printf("%s\n", one);
strcat(three, one); // can only concat one at a time
printf("%s\n", three);
    return 0;
}